#!/usr/bin/env bash
# Exercises Bluetooth power-off across suspend with fake sysfs and a busctl stub.
set -euo pipefail

ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
HOOK="$ROOT/system_files/usr/lib/systemd/system-sleep/45-armada-bluetooth-sleep"
[[ -x "$HOOK" ]]
tmp="$(mktemp -d)"
trap 'rm -rf -- "$tmp"' EXIT

bt_class="$tmp/sys/class/bluetooth"
state_file="$tmp/run/armada/bluetooth-powered-off"
bus_state="$tmp/bus"
calls="$tmp/calls"
mkdir -p "$bus_state"

add_adapter() {
    local adapter=$1 powered=$2 wake=${3:-}
    local ctrl="$tmp/sys/devices/$adapter/serial0/serial0-0"
    mkdir -p "$bt_class/$adapter" "$ctrl/power" "$ctrl/../power"
    ln -sfn "$ctrl" "$bt_class/$adapter/device"
    [[ -n "$wake" ]] && printf '%s\n' "$wake" >"$ctrl/../power/wakeup"
    printf '%s\n' "$powered" >"$bus_state/$adapter"
}

# Minimal busctl: get-property reads, Set writes, every call is logged.
cat >"$tmp/busctl" <<EOF
#!/usr/bin/env bash
printf '%s\n' "\$*" >>"$calls"
for arg in "\$@"; do
    case "\$arg" in /org/bluez/*) adapter=\${arg##*/} ;; esac
done
[[ -e "$bus_state/fail-\$adapter" && " \$* " == *" Set "* ]] && exit 1
if [[ " \$* " == *" get-property "* ]]; then
    [[ -r "$bus_state/\$adapter" ]] || exit 1
    printf 'b %s\n' "\$(<"$bus_state/\$adapter")"
elif [[ " \$* " == *" Set "* ]]; then
    printf '%s\n' "\${@: -1}" >"$bus_state/\$adapter"
fi
EOF
chmod +x "$tmp/busctl"

run_hook() {
    env ARMADA_RUN_DIR="$tmp/run/armada" ARMADA_BLUETOOTH_CLASS_DIR="$bt_class" \
        ARMADA_BUSCTL="$tmp/busctl" bash "$HOOK" "$@" 2>>"$tmp/hook.log"
}

add_adapter hci0 true
add_adapter hci1 false
add_adapter hci2 true enabled

# Powered adapters without wake are switched off; others are left alone.
run_hook pre suspend
[[ "$(<"$bus_state/hci0")" == false ]]
[[ "$(<"$bus_state/hci1")" == false ]]
[[ "$(<"$bus_state/hci2")" == true ]]
[[ "$(<"$state_file")" == hci0 ]]

# Resume restores only what the hook turned off, without waiting for BlueZ.
: >"$calls"
run_hook post suspend
[[ "$(<"$bus_state/hci0")" == true && "$(<"$bus_state/hci1")" == false ]]
grep -q -- '--expect-reply=no' "$calls"
[[ ! -e "$state_file" ]]

# A failed power-off is still recorded, so resume powers the adapter back on.
touch "$bus_state/fail-hci0"
printf 'true\n' >"$bus_state/hci0"
: >"$calls"
run_hook pre suspend
grep -q ' get-property ' "$calls"
[[ "$(<"$state_file")" == hci0 ]]
rm -f "$bus_state/fail-hci0"
run_hook post suspend
[[ ! -e "$state_file" ]]

# A stale entry left by a missed resume is not duplicated.
mkdir -p "$(dirname "$state_file")"
printf 'hci0\n' >"$state_file"
run_hook pre suspend
[[ "$(<"$state_file")" == hci0 ]]
run_hook post suspend
[[ "$(<"$bus_state/hci0")" == true ]]

# BlueZ unavailable: nothing is recorded or changed.
rm -f "$bus_state/hci0"
run_hook pre suspend
[[ ! -e "$state_file" ]]
printf 'true\n' >"$bus_state/hci0"

# Only valid adapter names in the state file are restored.
printf 'hci0\n../evil\n' >"$state_file"
: >"$calls"
run_hook post suspend
! grep -q evil "$calls"
[[ ! -e "$state_file" ]]

# Ignore unrelated sleep operations.
: >"$calls"
run_hook pre hibernate
run_hook post hibernate
[[ ! -s "$calls" && ! -e "$state_file" ]]

echo "bluetooth sleep hook tests passed"
