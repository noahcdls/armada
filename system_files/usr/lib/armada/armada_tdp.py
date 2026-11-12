"""Whole-device power limit for Steam's TDP slider (TdpLimit1).

Qualcomm has no package power cap to write, so armada-powerd closes the loop
itself: the battery fuel gauge gives measured device power, and the running
game is clamped with per-task uclamp.max (schedutil then caps the frequency it
asks for) plus a GPU devfreq ceiling. The Steam UI is never clamped, so the
QAM and Steam menu keep full speed while a limit is held.
"""

import ctypes
import os
import platform
import struct
from pathlib import Path

POWER_SUPPLY = Path("/sys/class/power_supply")
UCLAMP_SCALE = 1024
UCLAMP_FLOOR = 64

# struct sched_attr, SCHED_ATTR_SIZE_VER1
SCHED_ATTR_FMT = "=IIQiIQQQII"
SCHED_ATTR_SIZE = struct.calcsize(SCHED_ATTR_FMT)
SCHED_FLAG_KEEP_POLICY = 0x08
SCHED_FLAG_KEEP_PARAMS = 0x10
SCHED_FLAG_UTIL_CLAMP_MAX = 0x40
SYSCALLS = {"aarch64": (274, 275), "x86_64": (314, 315)}

# Controller tuning. Over target drops fast, under target rises slowly, and the
# band between holds still so the GPU ceiling does not flap.
DEADBAND_OVER = 0.03
DEADBAND_UNDER = 0.08
GAIN_DOWN = 0.5
GAIN_UP = 0.25
MAX_STEP_DOWN = 0.15
MAX_STEP_UP = 0.05
MIN_STEP = 0.01


def read_text(path, default=""):
    try:
        return Path(path).read_text().strip()
    except OSError:
        return default


def battery_path(root=POWER_SUPPLY):
    for supply in sorted(Path(root).glob("*")):
        if read_text(supply / "type") == "Battery" and (supply / "current_now").exists():
            return supply
    return None


def battery_watts(supply):
    # power_now on SM8750 reports a system rail (~57 W), so use I*V like MangoHud.
    if supply is None:
        return None
    try:
        current = int(read_text(supply / "current_now"))
        voltage = int(read_text(supply / "voltage_now"))
    except ValueError:
        return None
    watts = abs(current) * abs(voltage) / 1e12
    return watts if watts > 0 else None


def next_level(level, watts, target, min_level):
    """One controller step: the new clamp level in [min_level, 1]."""
    if not target or watts is None:
        return level
    error = (watts - target) / target
    if error > DEADBAND_OVER:
        level -= min(MAX_STEP_DOWN, max(MIN_STEP, GAIN_DOWN * error))
    elif error < -DEADBAND_UNDER:
        level += min(MAX_STEP_UP, max(MIN_STEP, GAIN_UP * -error))
    return min(1.0, max(min_level, level))


def level_uclamp(level):
    return max(UCLAMP_FLOOR, min(UCLAMP_SCALE, round(level * UCLAMP_SCALE)))


def _comm(pid):
    try:
        with open(f"/proc/{pid}/comm", encoding="utf-8") as f:
            return f.read().strip()
    except OSError:
        return ""


def _cmdline(pid):
    try:
        with open(f"/proc/{pid}/cmdline", "rb") as f:
            return f.read().split(b"\0")
    except OSError:
        return []


def steam_launch_pids():
    """Steam's reaper processes, one per running game (SteamLaunch AppId=...)."""
    pids = []
    for entry in os.listdir("/proc"):
        if entry.isdigit() and _comm(entry) == "reaper" and b"SteamLaunch" in _cmdline(entry):
            pids.append(int(entry))
    return pids


def game_tids(descendants):
    """Every thread of every process under Steam's game reapers."""
    tids = []
    for reaper in steam_launch_pids():
        for pid in descendants(reaper):
            try:
                tids.extend(int(t) for t in os.listdir(f"/proc/{pid}/task") if t.isdigit())
            except OSError:
                continue
    return tids


class Uclamp:
    """Per-task uclamp.max through sched_setattr(2); no cgroup moves needed."""

    def __init__(self):
        numbers = SYSCALLS.get(platform.machine())
        self.nr_set = numbers[0] if numbers else None
        self.libc = ctypes.CDLL(None, use_errno=True) if numbers else None
        self.applied = {}

    @property
    def available(self):
        return self.nr_set is not None

    def set_max(self, tid, value):
        attr = struct.pack(
            SCHED_ATTR_FMT, SCHED_ATTR_SIZE, 0,
            SCHED_FLAG_KEEP_POLICY | SCHED_FLAG_KEEP_PARAMS | SCHED_FLAG_UTIL_CLAMP_MAX,
            0, 0, 0, 0, 0, 0, value)
        buf = ctypes.create_string_buffer(attr, SCHED_ATTR_SIZE)
        if self.libc.syscall(self.nr_set, tid, buf, 0) != 0:
            return ctypes.get_errno()
        return 0

    def apply(self, tids, value):
        """Clamp tids to value; returns the first errno other than ESRCH, or 0."""
        if not self.available:
            return 0
        live = set(tids)
        for tid in list(self.applied):
            if tid not in live:
                del self.applied[tid]
        failure = 0
        for tid in tids:
            if self.applied.get(tid) == value:
                continue
            err = self.set_max(tid, value)
            if err == 0:
                self.applied[tid] = value
            elif err != 3 and not failure:
                failure = err
        return failure

    def release(self):
        if not self.available:
            return
        for tid in list(self.applied):
            self.set_max(tid, UCLAMP_SCALE)
        self.applied = {}
