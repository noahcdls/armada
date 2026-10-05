# Patches

Patches applied on top of BASE.env. Each entry's `source` is an upstream URL pinned
to a commit, or `armada` if it's original; a URL source with no `notes` is verbatim.
`notes` mean the file was modified.

- `patches/0001-Qualcomm-GPU-support.patch`
  source: https://github.com/ROCKNIX/distribution/blob/eb5f4c61271406b61ff21d668aad0d61d635d29e/projects/ROCKNIX/packages/apps/mangohud/patches/qualcomm/0001-Qualcomm-GPU-support.patch
- `patches/0002-GPU-monitoring.patch`
  source: armada
- `patches/0003-Battery-name.patch`
  source: https://github.com/ROCKNIX/distribution/blob/ae5151e7ddeadf3e2fc56ec03492e951e439204a/projects/ROCKNIX/packages/apps/mangohud/patches/common/0002-Battery-name.patch
- `patches/0004-Qualcomm-battery-power-now.patch`
  source: https://github.com/ROCKNIX/distribution/blob/eb5f4c61271406b61ff21d668aad0d61d635d29e/projects/ROCKNIX/packages/apps/mangohud/patches/qualcomm/0002-Qualcomm-battery-power_now.patch
- `patches/0005-RAM-name.patch`
  source: https://github.com/ROCKNIX/distribution/blob/688884af239b13832a928248b3555c36f8d44c31/projects/ROCKNIX/packages/apps/mangohud/patches/common/0003-RAM-name.patch
- `patches/0006-SM8750-Battery.patch`
  source: https://github.com/ROCKNIX/distribution/blob/7e83d3c918fa52a241ce1e589d629c220af40e1a/projects/ROCKNIX/packages/apps/mangohud/patches/SM8750/0002-SM8750-Battery.patch
- `patches/0007-gpu_fdinfo-skip-unreadable-fdinfo.patch`
  source: armada
- `patches/0008-mangoapp-show-active-upscaler.patch`
  source: armada
- `patches/0009-mangoapp-pause-while-the-Steam-UI-is-focused.patch`
  source: armada
  notes: mangoapp drew an empty full-screen overlay every frame in the Steam UI (an extra scanout plane, mangoapp<->Xwayland wakeup storm, ~70 mA idle on the Odin 3). It now pauses while Steam is focused unless mangoapp_steam or steam_ui=1 in /etc/armada/performance-overlay.conf (armada-control "Show in Steam UI" toggle) opts back in, and polls the focused app 4x/s instead of per frame.
