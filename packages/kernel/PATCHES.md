# Patches

Patches applied on top of BASE.env. Each entry's `source` is a URL pinned to a
commit, or `armada` for original work; a URL source with no `notes` is verbatim.
`notes` explain modifications or important differences from linked upstream work.
A patch entry's `upstream` is `local` for an Armada-authored change, `unknown` when
no equivalent submission was found, or a permanent URL to the upstream submission.

- `patches/0002-qcom-dispcc-sm8550-Fix-disp_cc_mdss_mdp_clk_src.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8550/patches/linux/0002-qcom-dispcc-sm8550-Fix-disp_cc_mdss_mdp_clk_src.patch
  upstream: unknown
- `patches/0004-drm-msm-a6xx-Enable-IFPC-on-Adreno-740.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8550/patches/linux/0004-drm-msm-a6xx-Enable-IFPC-on-Adreno-740.patch
  upstream: unknown
- `patches/0010-msm-resource-cleanup.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/packages/linux/patches/7.0/0010-msm-resource-cleanup.patch
  upstream: unknown
  notes: Armada initialises cstate before the num_mixers reset it adds; the ROCKNIX version writes through an uninitialised pointer.
- `patches/0048-drm-msm-dsi-reparent-byte-pixel-src-to-xo-on-disable.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8750/patches/linux/0048-drm-msm-dsi-reparent-byte-pixel-src-to-xo-on-disable.patch
  upstream: unknown
- `patches/0048b-drm-msm-dsi-fix-pll-init-in-bonded-mode.patch`
  source: armada
  upstream: local
- `patches/0049-drm-msm-dpu-panel-opt-in-8bpc-dither.patch`
  source: armada
  upstream: local
  notes: Armada wrote this patch; it has not been submitted upstream.
- `patches/0066-drm-msm-dpu-enable-inline-rotation.patch`
  source: https://github.com/ROCKNIX/distribution/blob/60bb58c1db053255b700f3953b72d619ec5aa85d/projects/ROCKNIX/devices/SM8550/patches/linux/0066-drm-msm-dpu-enable-sm8550-inline-rotation.patch
  upstream: unknown
  notes: Armada merged the ROCKNIX SM8550, SM8650 and SM8750 patches into one for the combined kernel, with one shared feature mask and rotation config.
- `patches/0068-drm-msm-dpu-lutdma-dspp-igc-gamut.patch`
  source: armada
  upstream: local
- `patches/0733-drm-msm-dpu-Fix-GAMMA-LUT-for-sm8750-related-DPUs.patch`
  source: https://git.kernel.org/next/linux-next/c/3389406e6a032b92c4770380c4aeec8dbf38cfae
  upstream: https://lore.kernel.org/r/20260930152645.22194-1-robin.clark@oss.qualcomm.com
  notes: Ported onto 0068's SM8750 DSPP block, which now lists GC next to its IGC and gamut; drops 0068's comment that SM8750 GC is a LUT bus block, since upstream drives it through the plain GC registers.
- `patches/0069-dt-bindings-display-msm-dpu-lutdma-reg.patch`
  source: armada
  upstream: local
- `patches/0070-arm64-dts-qcom-dpu-lutdma-reg.patch`
  source: armada
  upstream: local
- `patches/0076-drm-msm-dpu-expose-abgr-xbgr-2101010-on-planes.patch`
  source: armada
  upstream: local
- `patches/0077-drm-msm-dpu-plane-igc-3d-lut-color-pipelines.patch`
  source: armada
  upstream: local
- `patches/0078-drm-msm-dpu-fix-vblank-timestamps-on-command-mode-panels.patch`
  source: armada
  upstream: local
- `patches/0078a-drm-msm-dpu-program-merge3d-for-command-mode.patch`
  source: https://github.com/RetroidPocket/linux/commit/b547718c91dbaf8fe27745afced8de00d1f7415b
  upstream: unknown
  notes: Unmodified Retroid fix that programs and flushes MERGE_3D for command-mode displays using two layer mixers. Required by the uncompressed 1280x960 Nova/Duo panel; otherwise DSI receives half a line and reports FIFO underflow.
- `patches/0016-rp5-smooth-brightness-adjustment.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8250/patches/linux/0016-rp5-smooth-brightness-adjustment.patch
  upstream: unknown
  notes: Armada limited the ROCKNIX brightness change to SM8250 panels. A [related upstream proposal](https://lore.kernel.org/r/20260706180753.408753-1-kavansmith82@gmail.com) uses a different implementation.
- `patches/0028-drm-panel-Add-panel-driver-for-Chipone-ICNA35XX-base.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8750/patches/linux/0028-drm-panel-Add-panel-driver-for-Chipone-ICNA35XX-base.patch
  upstream: https://lore.kernel.org/r/20260607-icna35xx-v4-2-64de514add34@gmail.com
  notes: The carried implementation differs from the linked upstream submission and is ported to Linux 7.2's managed DRM panel allocator.
- `patches/0051-gpu-panel-add-Pocket-ACE-panel-driver.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8550/patches/linux/0051-gpu-panel-add-Pocket-ACE-panel-driver.patch
  upstream: unknown
  notes: Ported to Linux 7.2's managed DRM panel allocator.
- `patches/0052-gpu-panel-add-Pocket-DMG-panel-driver.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8550/patches/linux/0052-gpu-panel-add-Pocket-DMG-panel-driver.patch
  upstream: unknown
  notes: Ported to Linux 7.2's managed DRM panel allocator.
- `patches/0055_Synaptics-TD4328-LCD-panel.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8550/patches/linux/0055_Synaptics-TD4328-LCD-panel.patch
  upstream: https://lore.kernel.org/r/20240424-ayn-odin2-initial-v1-4-e0aa05c991fd@gmail.com
  notes: The carried implementation predates the linked upstream submission and is ported to Linux 7.2's managed DRM panel allocator.
- `patches/0056_Xm-Plus-XM91080G-panel.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8550/patches/linux/0056_Xm-Plus-XM91080G-panel.patch
  upstream: unknown
  notes: Ported to Linux 7.2's managed DRM panel allocator.
- `patches/0057_DDIC-CH13726A-panel.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8550/patches/linux/0057_DDIC-CH13726A-panel.patch
  upstream: unknown
  notes: Retains additional compatibles and the 120 ms sleep-out delay, using Linux 7.2's managed DRM panel allocator.
- `patches/0059-drm-panel-add-brightness-levels-helper.patch`
  source: armada
  upstream: not submitted
- `patches/0060-drm-panel-icna35xx-luminance-linear-backlight-scale.patch`
  source: armada
  upstream: not submitted
- `patches/0060a-drm-panel-icna35xx-add-mangmi-pocket-max.patch`
  source: https://github.com/ROCKNIX/distribution/blob/807c74fc46c124891d8aa9b57a68533d38e9a6b2/projects/ROCKNIX/devices/SM8250/patches/linux/0057_Chipone-ICNA35XX-panel.patch
  upstream: unknown
  notes: Ports the Pocket Max init sequence, four vendor modes and per-panel shutdown delays onto Armada's Linux 7.2 managed-panel driver while retaining Armada's luminance-linear backlight scale.
- `patches/0518-ROCKNIX-odin3-panel-frame-length-calibration.patch`
  source: https://github.com/ROCKNIX/distribution/blob/abfdcfb57ff42180a50fca60a2a150641608d57e/projects/ROCKNIX/devices/SM8750/patches/linux/0518-ROCKNIX-odin3-panel-frame-length-calibration.patch
  upstream: unknown
  notes: Context refreshed onto Armada's 0060 and 0060a; the code is unchanged.
- `patches/0518a-drm-panel-icna35xx-serialise-live-frame-length-writes.patch`
  source: armada
  upstream: local
- `patches/0518b-drm-panel-icna35xx-calibrate-the-ICNA3512-frame-length.patch`
  source: armada
  upstream: local
- `patches/0105-dt-bindings-display-panel-retroid-il97680a.patch`
  source: https://github.com/RetroidPocket/linux/commit/9bfe85be2179d03338d09b8900f3b1916999ef15
  upstream: not submitted
- `patches/0105a-drm-panel-retroid-il97680a.patch`
  source: https://github.com/JPyke3/linux/commit/c102403bfcfe545d34e7124630f60e56d090753b
  upstream: not submitted
- `patches/0108-drm-msm-dpu-send-the-flip-event-after-the-vblank-irq.patch`
  source: https://github.com/portare-ch/portareos/blob/be06100b6d127692ed99401d23980fc04888ae01/projects/PortareOS/devices/SM8550/patches/linux/1098-drm-msm-dpu-send-the-flip-event-after-the-vblank-irq.patch
  upstream: unknown
  notes: Companion flip-event ordering fix for AVR; refreshed offsets for Armada and added the source link to the patch header. Armada restricts the kickoff-count wait to encoders that receive the vblank irq: a bonded DSI slave never does, so on dual-DSI panels (AYANEO Pocket S 2K) every commit hit the 50 ms timeout.
- `patches/0109-drm-panel-il97680a-defer-display-enable.patch`
  source: armada
  upstream: local
- `patches/0062-gpu-drm-panel-add-wt0630-panel.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8550/patches/linux/0062-gpu-drm-panel-add-wt0630-panel.patch
  upstream: https://lore.kernel.org/r/20260625-topic-sm8650-ayaneo-pocket-s2-r63419-v8-2-8570e692143e@linaro.org
  notes: Ported to Linux 7.2's managed DRM panel allocator.
- `patches/0063-gpu-drm-panel-add-wt0600-1k-panel.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8550/patches/linux/0063-gpu-drm-panel-add-wt0600-1k-panel.patch
  notes: Standalone single-DSI driver for the 1080x1920 60Hz WT0600 panel (Pocket S 1K) from ROCKNIX PR #3007.
- `patches/0104-drm-panel-Add-Retroid-Pocket-6-panel.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8550/patches/linux/0104-drm-panel-Add-Retroid-Pocket-6-panel.patch
  upstream: unknown
  notes: Ported to Linux 7.2's managed DRM panel allocator.
- `patches/0104a-drm-panel-visionox-vtdr6130-add-sm8250.patch`
  source: https://github.com/armada-os/armada/issues/327
  upstream: unknown
  notes: Adds support for Visionox VTDR6130 panel revisions found in the Retroid Pocket Flip 2, derived from the affected device's live Android device tree. Reuses the Pocket 6 initialization sequence and DSC configuration with the Flip 2 regulator supplies.
- `patches/0064_Mangmi-Air-Y-Pro-panel.patch`
  source: https://github.com/ROCKNIX/distribution/blob/807c74fc46c124891d8aa9b57a68533d38e9a6b2/projects/ROCKNIX/devices/SM8250/patches/linux/0064_Mangmi-Air-Y-Pro-panel.patch
  upstream: unknown
- `patches/0058_AYN-Odin2-Mini--backlight.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8550/patches/linux/0058_AYN-Odin2-Mini--backlight.patch
  upstream: unknown
  notes: Armada refreshed only the Makefile context for Linux 7.1's backlight object list; driver behavior is unchanged.
- `patches/0060-backlight-sy7758-make-the-enable-gpio-optional.patch`
  source: armada
  upstream: local
  notes: The SY7758 driver itself is upstream since Linux 7.3; this keeps Armada's optional enable GPIO. The upstream binding still lists `enable-gpios` as required, which only affects dtbs_check for the Pocket DS.
- `patches/0054-regulator-add-sgm3804-i2c-regulator-for-panel-power-.patch`
  source: armada
  upstream: local
  notes: Armada adds compatibility for existing flat fixed-5-V nodes; child-regulator nodes use the Linux 7.2 upstream behavior unchanged.
- `patches/0056-backlight-aw99706-enable-hwen-before-chip-id-read.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8750/patches/linux/0056-backlight-aw99706-enable-hwen-before-chip-id-read.patch
  upstream: unknown
- `patches/0057-backlight-aw99706-konkr-cfg7.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8750/patches/linux/0057-backlight-aw99706-konkr-cfg7.patch
  upstream: unknown
- `patches/0066-regulator-add-qcom-pm8150l-lcdb.patch`
  source: https://github.com/ROCKNIX/distribution/blob/807c74fc46c124891d8aa9b57a68533d38e9a6b2/projects/ROCKNIX/devices/SM8250/patches/linux/0066-regulator-add-qcom-pm8150l-lcdb.patch
  upstream: unknown
- `patches/0015-touchscreen-edt-ft5x06-allow-to-override-input-name.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8250/patches/linux/0015-touchscreen-edt-ft5x06-allow-to-override-input-name.patch
  upstream: https://lore.kernel.org/r/20260409-ft5x06-label-v1-1-21e8a9ae9a60@gmail.com
- `patches/0030-input-rmi4-add-reset-gpio.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8550/patches/linux/0030-input-rmi4-add-reset-gpio.patch
  upstream: https://lore.kernel.org/r/20250210050220.634497-2-felix@kaechele.ca
- `patches/0032-rmi4-silence-spam-irq-errors.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8550/patches/linux/0032-rmi4-silence-spam-irq-errors.patch
  upstream: unknown
- `patches/0053-add-hynitron-touchscreen.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8550/patches/linux/0053-add-hynitron-touchscreen.patch.disabled
  upstream: unknown
  notes: Armada retains this disabled ROCKNIX driver for the Pocket DMG and refreshed only its Makefile context for Linux 7.1's Himax entry; driver behavior is unchanged.
- `patches/0053a-input-hynitron-port-to-gpiod.patch`
  source: armada
  upstream: local
  notes: Armada added this follow-up because Linux 7.1 removed the legacy OF GPIO-number API; it ports the retained Hynitron driver to GPIO descriptors.
- `patches/0053b-input-hynitron-restore-gpio-init-order.patch`
  source: armada
  upstream: local
  notes: Armada added this follow-up to preserve the vendor driver's pinctrl, GPIO-direction, power, and reset ordering after the GPIO-descriptor port.
- `patches/0065-input-touchscreen-add-hynitron-cst66xx.patch`
  source: https://github.com/ROCKNIX/distribution/blob/807c74fc46c124891d8aa9b57a68533d38e9a6b2/projects/ROCKNIX/devices/SM8250/patches/linux/0065-input-touchscreen-add-hynitron-cst66xx.patch
  upstream: unknown
- `patches/0054-input-goodix-override-resolution-from-dt.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8550/patches/linux/0054-input-goodix-override-resolution-from-dt.patch
  upstream: unknown
  notes: Armada replaced ROCKNIX's automatic resolution-mismatch heuristic and hardcoded fallback with explicit `goodix,native-size-x` and `goodix,native-size-y` properties. Scaling is dormant unless a device opts in with both native and standard touchscreen dimensions.
- `patches/0054a-dt-bindings-input-goodix-document-input-device-label.patch`
  source: armada
  upstream: local
  notes: Documents the optional Goodix `label` property used to name the input device.
- `patches/0054b-input-goodix-allow-overriding-input-device-name.patch`
  source: armada
  upstream: local
  notes: Allows the Pocket DS lower GT911 to expose its `bottom_touchscreen` label as the input device name.
- `patches/0029-Input-edt-ft5x06-add-no_regmap_bulk_read-option.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8750/patches/linux/0029-Input-edt-ft5x06-add-no_regmap_bulk_read-option.patch
  upstream: https://lore.kernel.org/r/20260723-b4-ft5426-v1-3-d4b4e32be042@gmail.com
- `patches/0059_AYN-Odin2-Mini--hynitron--cstxxx.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8550/patches/linux/0059_AYN-Odin2-Mini--hynitron--cstxxx.patch
  upstream: unknown
- `patches/0060-input-touchscreen-add-synaptics-dsx-kconfig.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8550/patches/linux/0060-input-touchscreen-add-synaptics-dsx-kconfig.patch
  upstream: unknown
- `patches/0060-input-touchscreen-add-synaptics-dsx-driver.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8550/patches/linux/0060-input-touchscreen-add-synaptics-dsx-driver.patch
  upstream: unknown
- `patches/0058-input-joystick-add-ayaneo-mcu-joystick.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8750/patches/linux/0058-input-joystick-add-ayaneo-mcu-joystick.patch
  upstream: unknown
- `patches/0069-input-misc-add-konkr-sysbtn-MCU-system-buttons.patch`
  source: https://github.com/ROCKNIX/distribution/blob/024028b4f3fdd139ae1e575efb25914b8f76595d/projects/ROCKNIX/devices/SM8750/patches/linux/0069-input-misc-add-konkr-sysbtn-MCU-system-buttons.patch
  upstream: unknown
  notes: Updated to ROCKNIX #3089, which adds the MCU-rendered stick lighting effects (sysfs "effect": static/breath/rainbow) and fixes the PM notifier to replay the active lighting mode after resume instead of only the last static colour.
- `patches/0069a-input-konkr-sysbtn-add-pocket-fit-mcu.patch`
  source: armada
  upstream: local
- `patches/0541-input-joystick-mcu-joystick-power-the-mcu-off-in-suspend.patch`
  source: armada
  upstream: local
- `patches/0060_Mangmi-Pocket-Max-SPI-joypad.patch`
  source: https://github.com/ROCKNIX/distribution/blob/807c74fc46c124891d8aa9b57a68533d38e9a6b2/projects/ROCKNIX/devices/SM8250/patches/linux/0060_Mangmi-Pocket-Max-SPI-joypad.patch
  upstream: unknown
- `patches/0060b-input-mangmi-pocket-max-keep-trigger-conversion-independent-of-calibration.patch`
  source: armada
  upstream: local
- `patches/0031_input--Add-driver-for-RSInput-Gamepad.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8550/patches/linux/0031_input--Add-driver-for-RSInput-Gamepad.patch
  upstream: unknown
- `patches/0508-input-rsinput-add-pm-resume-to-reinit-mcu-after-suspend.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8750/patches/linux/0508-input-rsinput-add-pm-resume-to-reinit-mcu-after-suspend.patch
  upstream: unknown
- `patches/0515-input-rsinput-reassemble-uart-frames-instead-of-dropping-them.patch`
  source: armada
  upstream: not submitted
  notes: serdev delivers arbitrary byte batches and the old parser dropped any batch that was not exactly one frame, visible as resume-correlated checksum mismatches on the rsinput gamepad devices.
- `patches/0504-Enable-64-bit-processes-to-use-compat-input-syscalls.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8250/patches/linux/0504-Enable-64-bit-processes-to-use-compat-input-syscalls.patch
  upstream: unknown
  notes: Armada rebased the unchanged compat-input prctl behavior onto Linux 7.1's current task-structure, UAPI, and prctl switch layout.
- `patches/0506-usbcore-add-interrupt-interval-override.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8550/patches/linux/0506-usbcore-add-interrupt-interval-override.patch
  upstream: unknown
- `patches/1008-HID-uhid-read-the-output-queue-under-qlock.patch`
  source: armada
  upstream: local
  notes: Fixes a NULL dereference in `uhid_char_read()` on arm64 that orphans InputPlumber's virtual controller and stalls Steam's controller thread until reboot. Mainline carries the same lockless read; this is a candidate for upstream submission.
- `patches/0071-HACK-fix-usb-boot-hang.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8550/patches/linux/0071-HACK-fix-usb-boot-hang.patch
  upstream: unknown
  notes: ROCKNIX carries this workaround in its SM8550 and SM8650 kernels. Armada preserves the normal xHCI readiness handshake on every other SoC.
- `patches/1000-input-misc-qcom-hv-haptics-sm8750.patch`
  source: https://github.com/ROCKNIX/distribution/blob/47e077d0bbc714abb05afea6b68144b6f28ee19a/projects/ROCKNIX/devices/SM8750/patches/linux/1000-input-misc-qcom-hv-haptics-sm8750.patch
  upstream: unknown
- `patches/1001-input-qcom-haptics-update-assign-str.patch`
  source: armada
  upstream: local
  notes: Armada updates the vendored driver for Linux 7.1's one-argument `__assign_str()` API.
- `patches/1001-haptics-driver-support-periodic-sine-and-fixes.patch`
  source: https://github.com/ROCKNIX/distribution/blob/47e077d0bbc714abb05afea6b68144b6f28ee19a/projects/ROCKNIX/devices/SM8750/patches/linux/1001-haptics-driver-support-periodic-sine-and-fixes.patch
  upstream: unknown
- `patches/1002-input-rsinput-sm8750-ff.patch`
  source: https://github.com/ROCKNIX/distribution/blob/47e077d0bbc714abb05afea6b68144b6f28ee19a/projects/ROCKNIX/devices/SM8750/patches/linux/1002-input-rsinput-sm8750-ff.patch
  upstream: unknown
  notes: Armada rebased ROCKNIX's force-feedback bridge because its final hunk is malformed and it targets a different RSInput revision. ROCKNIX enables rumble for every RSInput device; Armada gates it with a DT property set only by the supported SM8550 and SM8750 trees that also instantiate the Qualcomm haptics device. The SM8550 common tree intentionally covers both AYN and Retroid products.
- `patches/1003-input-haptics-fix-rumble-bridge-atomic-sleep.patch`
  source: armada
  upstream: local
  notes: The imported bridge called the haptics driver's sleeping upload, playback, and erase callbacks under spin_lock_irq, which emitted "BUG: scheduling while atomic" on every rumble stop and intermittently hard-locked the Odin 3 (reproduced on hardware). The bridge now serializes with a mutex and is process-context only, RSInput defers its atomic playback callback to a work item, and the haptics suspend path cancels the pending stop and set-gain workers so they cannot fire into resume. ROCKNIX carries the identical bug as of 2026-08-04; worth upstreaming once soak-tested.
- `patches/1004-input-haptics-stop-zero-amplitude-immediately.patch`
  source: armada
  upstream: local
  notes: The imported periodic-sine compatibility patch changed zero-amplitude updates to gain 1, then stopped the motor five seconds later. The configured brake pattern made that stop a distinct delayed tap. Zero-amplitude updates now erase immediately, a following playback request cannot restart stale motor state when no effect is loaded, and in-place gain updates balance their transient runtime-PM reference.
- `patches/1005-input-rsinput-quiesce-the-mcu-across-system-sleep.patch`
  source: https://github.com/shuuri-labs/pocknix-os/blob/d2544c1481b55e9dec18ff74a8751d4a67b351f8/kernel/sm8550/patches/20-sm8550/1004-input-rsinput-suspend-resume-gamepad-mcu.patch
  upstream: local
  notes: Carries only the suspend-side MCU quiesce from the source patch; the source's resume and pm_ops additions are omitted because this tree already has both and rsinput_init_commands() performs the full power-on itself.
- `patches/1006-tty-serial-qcom-geni-mask-non-console-irq-on-suspend.patch`
  source: https://github.com/thorch-os/thorch/blob/2614a262d7de3f31bd47a0c92981461146663847/packages/linux-thorch/patches/0010-tty-serial-qcom-geni-mask-non-console-irq-on-suspend.patch
  upstream: unknown
- `patches/1007-input-rsinput-drop-the-mcu-supply-across-system-sleep.patch`
  source: armada
  upstream: local
- `patches/1300-input-rsinput-axis-deadzone.patch`
  source: armada
  upstream: local
  notes: Armada replaced ROCKNIX's global experimental Odin 3 range and deadzone defaults with a per-device `axis-deadzone` property. The Odin 3 DTS supplies its range and deadzone explicitly.
- `patches/1301-input-rsinput-decouple-trigger-reference-from-calibration.patch`
  source: armada
  upstream: local
  notes: Keeps the RSInput MCU trigger release reference independent of the calibrated evdev maximum, fixing incomplete travel and deteriorating repeated calibration on AYN devices (issue #423).
- `patches/0059-ASoC-aw88395-lib-skip-monitor-sections-in-V1-ACF-parse.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8750/patches/linux/0059-ASoC-aw88395-lib-skip-monitor-sections-in-V1-ACF-parse.patch
  upstream: unknown
- `patches/0063-ASoC-wcd939x-route-usbss-on-integrated-jack-insert.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8750/patches/linux/0063-ASoC-wcd939x-route-usbss-on-integrated-jack-insert.patch
  upstream: unknown
- `patches/0064-ASoC-wcd-mbhc-clear-stale-jack-report-on-mechanical-removal.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8750/patches/linux/0064-ASoC-wcd-mbhc-clear-stale-jack-report-on-mechanical-removal.patch
  upstream: unknown
- `patches/0036_ASoC--qcom--sc8280xp-Add-support-for-Primary-I2S.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8550/patches/linux/0036_ASoC--qcom--sc8280xp-Add-support-for-Primary-I2S.patch
  upstream: https://lore.kernel.org/r/20251008-topic-sm8x50-next-hdk-i2s-v2-3-6b7d38d4ad5e@linaro.org
  notes: Rebased onto Linux 7.3, which handles MI2S formats and LPAIF sysclks in hw_params per card data. Keeps the optional `i2s_clk` board clock, now counted across all MI2S DAIs (the former 0060), and the Primary MI2S formats at startup for cards without `codec_dai_fmt` (SM8750).
- `patches/0032-ASoC-codecs-aw88166-AYN-Products-Specific-modificati.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8750/patches/linux/0032-ASoC-codecs-aw88166-AYN-Products-Specific-modificati.patch
  upstream: unknown
- `patches/0030-leds-Add-driver-for-HEROIC-HTR3212.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8750/patches/linux/0030-leds-Add-driver-for-HEROIC-HTR3212.patch
  upstream: unknown
- `patches/0061_leds-aw200xx-vdd-supply.patch`
  source: https://github.com/ROCKNIX/distribution/blob/807c74fc46c124891d8aa9b57a68533d38e9a6b2/projects/ROCKNIX/devices/SM8250/patches/linux/0061_leds-aw200xx-vdd-supply.patch
  upstream: unknown
- `patches/0054_sn3112-pwm-driver.patch`
  source: https://github.com/ROCKNIX/distribution/blob/4609c5017f350e6e2307ec909e328454d5bec062/projects/ROCKNIX/devices/SM8550/patches/linux/0054_sn3112-pwm-driver.patch
  upstream: https://lore.kernel.org/r/20240424-ayn-odin2-initial-v1-2-e0aa05c991fd@gmail.com
  notes: Includes ROCKNIX #3110's fix for the arm64 probe crash: set_bit()/clear_bit() on a cast uint8_t[3] alignment-faults under LSE atomics, replaced with plain bitwise ops under priv->lock. The matching Odin 2 DTS change re-enables the sn3112 nodes that were disabled to dodge the crash.
- `patches/0054c-pwm-sn3112-power-down-across-system-suspend.patch`
  source: armada
  upstream: local
- `patches/0734-dt-bindings-clock-qcom-gcc-sm8250-Add-CX-power-domai.patch`
  source: https://git.kernel.org/next/linux-next/c/98e936c9d46a25b4eceacf907fe5d87b3999040e
  upstream: https://patch.msgid.link/20260924-qcom-tie-cx-to-gcc-v5-3-38732033e5b5@oss.qualcomm.com
  notes: Replaces Neil Armstrong's earlier DT-only series (20260424) together with 0735-0741 and 0746-0748.
- `patches/0735-arm64-dts-qcom-sm8250-Add-GCC-CX-power-domain.patch`
  source: https://git.kernel.org/next/linux-next/c/389a0144c511316cf21d5dc2aa30028de87f9d00
  upstream: https://patch.msgid.link/20260924-qcom-tie-cx-to-gcc-v5-36-38732033e5b5@oss.qualcomm.com
- `patches/0736-dt-bindings-clock-qcom-sm8550-gcc-Add-CX-power-domai.patch`
  source: https://git.kernel.org/next/linux-next/c/5a577a480dd3d764cc2f55a112efc92d59ad59ec
  upstream: https://patch.msgid.link/20260924-qcom-tie-cx-to-gcc-v5-7-38732033e5b5@oss.qualcomm.com
- `patches/0737-clk-qcom-gcc-sm8550-Tie-the-CX-power-domain-to-contr.patch`
  source: https://git.kernel.org/next/linux-next/c/1f15b20e7c78641406746e8a9d6907c312c8d907
  upstream: https://patch.msgid.link/20260924-qcom-tie-cx-to-gcc-v5-24-38732033e5b5@oss.qualcomm.com
- `patches/0738-arm64-dts-qcom-sm8550-Add-GCC-CX-power-domain.patch`
  source: https://git.kernel.org/next/linux-next/c/df50f5c5690a472d750a0e327ac4d05a4a9c8b79
  upstream: https://patch.msgid.link/20260924-qcom-tie-cx-to-gcc-v5-39-38732033e5b5@oss.qualcomm.com
- `patches/0739-dt-bindings-clock-qcom-sm8650-gcc-Add-CX-power-domai.patch`
  source: https://git.kernel.org/next/linux-next/c/76615e10462c425f926e50dce52e9d23bb2f9428
  upstream: https://patch.msgid.link/20260924-qcom-tie-cx-to-gcc-v5-8-38732033e5b5@oss.qualcomm.com
- `patches/0740-clk-qcom-gcc-sm8650-Tie-the-CX-power-domain-to-contr.patch`
  source: https://git.kernel.org/next/linux-next/c/23d9b62d602e5429fd0147fdc0dc2aae15ed932c
  upstream: https://patch.msgid.link/20260924-qcom-tie-cx-to-gcc-v5-25-38732033e5b5@oss.qualcomm.com
- `patches/0741-arm64-dts-qcom-sm8650-Add-GCC-CX-power-domain.patch`
  source: https://git.kernel.org/next/linux-next/c/108a8d51fba8432c5d5253dec1c565ffe7c1edbc
  upstream: https://patch.msgid.link/20260924-qcom-tie-cx-to-gcc-v5-40-38732033e5b5@oss.qualcomm.com
- `patches/v3_20261002_anandu_e_misc_fastrpc_fix_context_leak_and_hang_on_signal_interrupted_invoke.patch`
  source: https://lore.kernel.org/r/20261002-anandu-fastrpc-interrupted-invoke-v3-v3-1-31e90439d2ba@oss.qualcomm.com
  upstream: https://lore.kernel.org/r/20261002-anandu-fastrpc-interrupted-invoke-v3-v3-1-31e90439d2ba@oss.qualcomm.com
  notes: Backported to 7.2's inline wait, and put_work_scheduled uses xchg() instead of fl->lock because the rpmsg callback runs in hard IRQ; the commit message still describes v3.
- `patches/0569-soc-qcom-smp2p-reset-inbound-state-only-on-restart.patch`
  source: armada
  upstream: local
- `patches/0504-mailbox-qcom-ipcc-mask-summary-irq-for-suspend-to-ram.patch`
  source: https://github.com/ROCKNIX/distribution/commit/f955f5b6137554253e4d52bbe72f9b4936fb253d
  upstream: not submitted
  notes: Reworked from ROCKNIX's blanket IRQF_NO_SUSPEND removal: the summary
  irq is masked (unlazy) only for suspend-to-RAM on the SM8550/SM8750
  compatibles, so suspend-to-idle keeps the doorbell live and charging can
  start while asleep.
- `patches/0505-msm_gem-lock-before-put_iova_spaces.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8250/patches/linux/0505-msm_gem-lock-before-put_iova_spaces.patch
  upstream: unknown
- `patches/0204-thermal-qcom-tsens-mask-lower-threshold-irqs-across-suspend.patch`
  source: armada
  upstream: local
  notes: Lower threshold crossings during the suspend transition cannot be serviced while thermal zones are quiesced, so the level IRQ storms and aborts suspend; masking LOWER across the transition removes the cause and keeps upper/critical wake armed.
- `patches/0510-soc-qcom-ice-unwind-clocks-on-resume-failure.patch`
  source: armada
  upstream: local
- `patches/0511-scsi-ufs-qcom-reenable-irq-on-host-reset-failure.patch`
  source: armada
  upstream: local
- `patches/0533-scsi-ufs-ufs-qcom-enable-only-lane-clocks-in-lane-clock-apis.patch`
  source: https://git.kernel.org/pub/scm/linux/kernel/git/mkp/scsi.git/commit/?id=f07317a8d57f382ec505597816271dd72ffa20c7
  upstream: https://git.kernel.org/pub/scm/linux/kernel/git/mkp/scsi.git/commit/?id=f07317a8d57f382ec505597816271dd72ffa20c7
- `patches/0535-scsi-ufs-core-fast-abort-unsupported-query-idns.patch`
  source: https://git.kernel.org/pub/scm/linux/kernel/git/mkp/scsi.git/commit/?id=d1fa5cea5dcd72a9ec21b835c572a28c0c3f4fbf
  upstream: https://git.kernel.org/pub/scm/linux/kernel/git/mkp/scsi.git/commit/?id=d1fa5cea5dcd72a9ec21b835c572a28c0c3f4fbf
- `patches/0536-scsi-ufs-core-dynamically-disable-timestamp-on-unsupported-devices.patch`
  source: https://git.kernel.org/pub/scm/linux/kernel/git/mkp/scsi.git/commit/?id=00eec343c7306be7f1103f5002abd77496937ff9
  upstream: https://git.kernel.org/pub/scm/linux/kernel/git/mkp/scsi.git/commit/?id=00eec343c7306be7f1103f5002abd77496937ff9
- `patches/0537-usb-xhci-pci-renesas-let-the-controller-power-off-in-suspend.patch`
  source: armada
  upstream: local
- `patches/0566-clk-qcom-gcc-sm8550-let-the-pcie-gdscs-collapse-in-suspend.patch`
  source: armada
  upstream: local
- `patches/0567-clk-qcom-gcc-sm8650-let-the-pcie-gdscs-collapse-in-suspend.patch`
  source: armada
  upstream: local
- `patches/0568-arm64-dts-qcom-sm8250-cpu-ddr-votes-active-only.patch`
  source: https://github.com/kettlelinux/kettlelinux/blob/c2849b95b3af9bf6d1d52cefa1e66167a22c86b4/kernel/patches/21-sm8250/0114-arm64-dts-qcom-sm8250-cpu-ddr-votes-active-only.patch
  upstream: unknown
  notes: Context refreshed for the 7.3 includes.
- `patches/0512-PCI-qcom-skip-L23-ready-poll-on-SM8550.patch`
  source: armada
  upstream: local
- `patches/0513-PCI-qcom-honour-an-opp-suspend-opp-as-the-non-s2ram-memory-floor.patch`
  source: armada
  upstream: not submitted
  notes: On OPP-scaling platforms the OPP carries the only PCIe memory-path votes, so dropping it to NULL on non-S2RAM suspend leaves the RPMh sleep set with no DDR/LLCC contract and the AOP never resumes. Deliberately does not populate `pcie->icc_mem` on OPP platforms: `qcom_pcie_icc_opp_update()` prefers an `icc_mem` handle over the OPP branch, so providing one silently disables the post-link-training OPP update and pins the OPP at the probe-time maximum.
- `patches/0522-PCI-host-common-let-only-endpoints-veto-d3cold.patch`
  source: armada
  upstream: local
- `patches/0523-regulator-qcom-rpmh-add-suspend-state-support.patch`
  source: https://github.com/thorch-os/thorch/blob/82e7472e6cad5c08a55c3aef92ef5be218621b2c/packages/linux-thorch/patches/0218-regulator-qcom-rpmh-add-suspend-state-support.patch
  upstream: unknown
  notes: Uses the PMIC's own bypass mode (`pmic_bypass_mode`) instead of `PMIC4_BOB_MODE_PASS`, which is wrong on PMIC5.
- `patches/0524-regulator-core-apply-mem-state-for-s2idle.patch`
  source: https://github.com/thorch-os/thorch/blob/82e7472e6cad5c08a55c3aef92ef5be218621b2c/packages/linux-thorch/patches/0219-regulator-core-apply-mem-state-for-s2idle.patch
  upstream: unknown
- `patches/0525-regulator-core-log-missing-suspend-configuration-at-debug.patch`
  source: armada
  upstream: local
- `patches/0526-regulator-apply-state-mem-in-s2idle-only-for-opted-in-drivers.patch`
  source: armada
  upstream: local
- `patches/0541-soc-qcom-add-a-suspend-breadcrumb-trail.patch`
  source: armada
  upstream: local
- `patches/0543-PCI-qcom-let-the-suspend-opp-floor-be-skipped-for-debugging.patch`
  source: armada
  upstream: local
- `patches/0544-interconnect-qcom-bcm-voter-debug-sleep-keepalive-for-named-bcms.patch`
  source: armada
  upstream: local
  notes: Test knob. icc_bcm_voter.sleep_keepalive_bcms (default empty) keeps a one-unit sleep vote on the listed BCMs, to find the minimal suspend floor. `SN4` restores the old SM8750 sleep keepalive at runtime if an s2idle wake hang ever needs ruling out.
- `patches/0514-PCI-qcom-honor-iommu-map-cell-count.patch`
  source: https://lkml.iu.edu/2609.0/16096.html
  upstream: https://lore.kernel.org/r/20260907143349.317495-1-mani@kernel.org
- `patches/0514a-of-property-honor-iommu-cells-in-iommu-map-devlinks.patch`
  source: armada
  upstream: local
- `patches/0001-pcie-update-sm8550-dtsi.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8550/patches/linux/0001-pcie-update-sm8550-dtsi.patch
  upstream: https://lore.kernel.org/r/20260611-wake-v2-33-2744251b1181@oss.qualcomm.com
- `patches/0120-20250728_konradybcio_gpu_cc_power_requirements_reality_check.patch`
  source: https://github.com/ROCKNIX/distribution/blob/ef264a238d5e2ba960145e3fda663dc27de49a80/projects/ROCKNIX/devices/SM8550/patches/linux/0120-20250728_konradybcio_gpu_cc_power_requirements_reality_check.patch
  upstream: https://lore.kernel.org/r/20250728-topic-gpucc_power_plumbing-v1-22-09c2480fe3e6@oss.qualcomm.com
- `patches/0121-pmdomain-qcom-rpmhpd-presync-floor-gmu-rails.patch`
  source: https://github.com/ROCKNIX/distribution/blob/ef264a238d5e2ba960145e3fda663dc27de49a80/projects/ROCKNIX/devices/SM8550/patches/linux/0121-pmdomain-qcom-rpmhpd-presync-floor-gmu-rails.patch
  source: https://github.com/ROCKNIX/distribution/blob/ef264a238d5e2ba960145e3fda663dc27de49a80/projects/ROCKNIX/devices/SM8750/patches/linux/0052-pmdomain-qcom-rpmhpd-presync-floor-gmu-rails.patch
  upstream: unknown
  notes: Armada applies the presync_floor and skip_retention_level flags via private descriptors (gfx_gmu for SM8550+SM8750, gmxc_sm8750) so GMU rail pre-sync behavior cannot change on other SoCs; ROCKNIX instead flags the shared gfx/gmxc structs, which would leak onto every SoC sharing them in a combined kernel. SM8250 and SM8650 have no Linux-side voter on these rails (their gpucc/gmu nodes reference only gpucc GDSCs), so the flags would be inert there today; revisit the scoping if the upstream gpucc power plumbing series lands and adds voters on more SoCs.
- `patches/0122-interconnect__qcom__sm8550__Enable_QoS_configuration.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8550/patches/linux/0122-interconnect__qcom__sm8550__Enable_QoS_configuration.patch
  upstream: unknown
- `patches/0200-ASoC-wcd938x-add-DMIC-DAPM-inputs.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8550/patches/linux/0200-ASoC-wcd938x-add-DMIC-DAPM-inputs.patch
  upstream: unknown
- `patches/1020-wifi-ath12k-send-the-computed-scan-priority-to-the-f.patch`
  source: https://github.com/ROCKNIX/distribution/blob/10b09e8df73b2b07ff04a243ded7425e41cd67fa/projects/ROCKNIX/devices/SM8550/patches/linux/1020-wifi-ath12k-send-the-computed-scan-priority-to-the-f.patch
  upstream: unknown
- `patches/1021-wifi-ath12k-convert-scan-timeout-to-wiphy-delayed-work.patch`
  source: https://lkml.iu.edu/2609.1/17957.html
  upstream: https://lkml.iu.edu/2609.1/17957.html
- `patches/1030-media-iris-send-the-stream-POC-type.patch`
  source: armada
  upstream: local
- `patches/1031-media-iris-stop-AV1-tier-overwriting-HEVC-tier.patch`
  source: armada
  upstream: local
- `patches/v9_20260801_sachin_garg_media_iris_cache_work_mode_in_iris_set_stage.patch`
  source: https://lore.kernel.org/r/20260801-iris_multi_slice-v9-1-bddf1449c280@oss.qualcomm.com
  upstream: https://lore.kernel.org/r/20260801-iris_multi_slice-v9-1-bddf1449c280@oss.qualcomm.com
- `patches/1032-media-iris-count-CABAC-cost-in-the-decoder-VSP-clock.patch`
  source: armada
  upstream: local
- `patches/1033-media-iris-add-decoder-display-delay-controls.patch`
  source: armada
  upstream: local
- `patches/1034-media-iris-decode-in-stage-1-for-decode-order.patch`
  source: armada
  upstream: local
- `patches/1035-media-iris-run-decode-order-sessions-at-the-highest-clock.patch`
  source: armada
  upstream: local
- `patches/1036-media-iris-only-rescale-decoder-power-on-bitstream-queue.patch`
  source: armada
  upstream: local
- `patches/1037-media-iris-decode-in-stage-1-at-the-top-clock-by-default.patch`
  source: armada
  upstream: local
- `patches/1370-media-iris-a-resolution-change-last-buffer-is-not-an-error.patch`
  source: https://github.com/kettlelinux/kettlelinux/blob/2b7661b4d937d7efbb487c4bba84f8705be7cc5d/kernel/patches/40-kettle/1370-media-iris-a-resolution-change-last-buffer-is-not-an-error.patch
  upstream: unknown
- `patches/0500-ROCKNIX-set-boot-fanspeed.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8550/patches/linux/0500-ROCKNIX-set-boot-fanspeed.patch
  upstream: unknown
- `patches/0501-ROCKNIX-fix-wifi-and-bt-mac.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8550/patches/linux/0501-ROCKNIX-fix-wifi-and-bt-mac.patch
  upstream: unknown
  notes: Armada refreshed only the ath12k insertion context for Linux 7.1's rate-table macros; MAC derivation behavior is unchanged.
- `patches/0503-ROCKNIX-battery-name.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8550/patches/linux/0503-ROCKNIX-battery-name.patch
  upstream: unknown
- `patches/0901-power-supply-qcom-battmgr-fix-charge-unit.patch`
  source: https://lkml.iu.edu/2608.3/10893.html
  upstream: https://lkml.iu.edu/2608.3/10893.html
  notes: Carries the upstream SM8350-class fix that initializes the charge unit to mAh so CHARGE_FULL* is available to userspace.
- `patches/0902-power-supply-qcom-battmgr-expose-charge-now.patch`
  source: https://lkml.iu.edu/2608.3/10890.html
  upstream: https://lkml.iu.edu/2608.3/10890.html
  notes: Carries the upstream SM8350/SM8550 mapping of the firmware remaining-charge counter to CHARGE_NOW.
- `patches/0903-power-supply-qcom-battmgr-expose-the-charge-current-limit.patch`
  source: armada
  upstream: local
- `patches/0904-power-supply-qcom-battmgr-report-charge-threshold-set-failures.patch`
  source: armada
  upstream: local
- `patches/0910-firmware-qcom-scm-allow-QSEECOM-on-OpenABL-s-platforms.patch`
  source: https://github.com/OpenHandheldCollective/OpenABL/blob/8f09253f8f93e7d9ff0b5baf3bda87976f0c54ac/Linux/0001-firmware-qcom-scm-allow-QSEECOM-on-OpenABL-s-platforms.patch
  upstream: unknown
  notes: Upstream tested it on SM6115 only. Armada needs it for SM8250, SM8550, SM8650 and SM8750, where OpenABL keeps its settings in UEFI variables.
- `patches/0001-pcie-update-sm8650-dtsi.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8650/patches/linux/0001-pcie-update-sm8650-dtsi.patch
  upstream: https://lore.kernel.org/r/20260611-wake-v2-35-2744251b1181@oss.qualcomm.com
- `patches/0006-add-hw_params-callback-function-to-drm_connector_hdmi_audio_ops.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8550/patches/linux/0006-add-hw_params-callback-function-to-drm_connector_hdmi_audio_ops.patch
  upstream: https://lore.kernel.org/r/20250925040530.20731-1-liujianfeng1994@gmail.com
- `patches/0010-ASoC-qcom-add-KONKR-Pocket-FIT-WSA2-card.patch`
  source: armada
  upstream: local
  notes: Pocket FIT uses the same WSA2-only speaker wiring as Pocket S2. Armada adds a board-specific compatible backed by the accepted Pocket S2 channel mapping.
- `patches/0011-ASoC-qcom-audioreach-use-wsa-interface-for-sm8650-wsa2.patch`
  source: armada
  upstream: local
  notes: Restores the WSA2-to-WSA interface rewrite that ROCKNIX bundled inside its replaced channel-map workaround; the SM8650 topology declares the speaker backend as WSA2, which the shipped ADSP firmware rejects. Gated to `qcom,sm8650`; remove once a corrected topology stops declaring WSA2.
- `patches/0063-gpu-drm-panel-add-pocket-fit-panel.patch`
  source: https://github.com/ROCKNIX/distribution/blob/5cff2f7918ca6bd56d8a884f0837309529a058bc/projects/ROCKNIX/devices/SM8750/patches/linux/0055-gpu-drm-panel-add-pocket-fit-panel.patch
  upstream: unknown
  notes: Uses the four-mode SM8750 variant and Linux 7.2's managed DRM panel allocator.
- `patches/0064-input-touchscreen-add-rocknix-chipone-tddi.patch`
  source: https://github.com/ROCKNIX/chipone_tddi/commit/af27029fa2b27c4a77d16809298ed5d03c9da5a6
  upstream: unknown
  notes: ROCKNIX ships this full driver as an out-of-tree module for the SM8650 KONKR Pocket FIT. Armada converts the pinned fork to an in-tree patch; its C and header files are unchanged, while Kconfig and Kbuild are adapted for the combined kernel. The fork includes ROCKNIX's Linux 7.1 GPIO compatibility update.
- `patches/0014-sm8250-ath11k-fix-wifi-mac.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8250/patches/linux/0014-fix-wifi-and-bt-mac.patch
  upstream: unknown
  notes: Armada carries only the ath11k portion of the shared ROCKNIX patch; the Bluetooth and SoC-serial changes are supplied by `0501-ROCKNIX-fix-wifi-and-bt-mac.patch`.
- `patches/0067-arm64-dts-qcom-pm8150l-add-lcdb-node.patch`
  source: https://github.com/ROCKNIX/distribution/blob/063e530e58d380aa17a7c608f0853898cc3911a5/projects/ROCKNIX/devices/SM8250/patches/linux/0067-arm64-dts-qcom-pm8150l-add-lcdb-node.patch
  upstream: unknown
- `patches/0004-pm8150b.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8250/patches/linux/0004-pm8150b.patch
  upstream: unknown
- `patches/0009-qcom-spmi-haptics.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8250/patches/linux/0009-qcom-spmi-haptics.patch
  upstream: unknown
  notes: Armada refreshed only the Kconfig insertion context so the SM8250 haptics driver follows Linux 7.1's high-voltage haptics entry; driver behavior is unchanged.
- `patches/0008-retroid-gamepad.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8250/patches/linux/0008-retroid-gamepad.patch
  upstream: unknown
- `patches/0013-add-force-feedback.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8250/patches/linux/0013-add-force-feedback.patch
  upstream: unknown
- `patches/0008a-input-retroid-keep-trigger-conversion-independent-of-calibration.patch`
  source: armada
  upstream: local
- `patches/0063_Mangmi-Pocket-Max-HL7139-charge-pump.patch`
  source: https://github.com/ROCKNIX/distribution/blob/807c74fc46c124891d8aa9b57a68533d38e9a6b2/projects/ROCKNIX/devices/SM8250/patches/linux/0063_Mangmi-Pocket-Max-HL7139-charge-pump.patch
  upstream: unknown
- `patches/0011-qcom-pm8150b-charger.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8250/patches/linux/0011-qcom-pm8150b-charger.patch
  upstream: unknown
  notes: Armada refreshed only the Makefile context for Linux 7.2's expanded Surface power-supply entries; charger and fuel-gauge behavior is unchanged.
- `patches/0005-sm8250-uart.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8250/patches/linux/0005-sm8250-uart.patch
  upstream: unknown
- `patches/9998-sm8250-gpu-tuning.patch`
  source: https://github.com/ROCKNIX/distribution/blob/f3e2b6187cd2ae2dc5122edfebe84228a314f2c5/projects/ROCKNIX/devices/SM8250/patches/linux/9998-gpu-tuning.patch
  upstream: unknown
  notes: Contents are verbatim; Armada renamed the file from the ROCKNIX `9998-gpu-tuning.patch`.
- `patches/0001-msm-dsi-restore-wide_bus-bpp-calculation.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8250/patches/linux/0001-msm-dsi-restore-wide_bus-bpp-calculation.patch
  upstream: unknown
  notes: Armada limited the ROCKNIX change to SM8250 so it does not alter the shared DSI path on other supported SoCs.
- `patches/0012-ASoC-qcom-q6asm-dai-Change-some-default-periods.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8250/patches/linux/0012-ASoC-qcom-q6asm-dai-Change-some-default-periods.patch
  upstream: unknown
- `patches/0062_wsa881x-shared-powerdown-gpio.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8250/patches/linux/0062_wsa881x-shared-powerdown-gpio.patch
  upstream: unknown
  notes: Ported to Linux 7.2's `GPIOD_OUT_LOW` initialization while retaining the non-exclusive request needed by boards whose two amplifiers share one powerdown GPIO.
- `patches/0100-revert-force-16bit-audio.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8250/patches/linux/0100-revert-force-16bit-audio.patch
  upstream: unknown
- `patches/0300-batocera-fix-headphone-jack-detection.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8250/patches/linux/0300-batocera-fix-headphone-jack-detection.patch
  upstream: unknown
  notes: Armada limited the ROCKNIX headphone-jack workaround to SM8250 so it does not alter shared codec behavior on other supported SoCs.
- `patches/0102-arm64-dts-qcom-pm8150-Add-nvmem-support-for-PM8150-R.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8250/patches/linux/0102-arm64-dts-qcom-pm8150-Add-nvmem-support-for-PM8150-R.patch
  upstream: unknown
- `patches/9999-sm8250-disable-coresight-stm.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8250/patches/linux/9999-remove-log-spam.patch
  upstream: unknown
  notes: Armada carries only the ROCKNIX device-tree change that disables CoreSight STM and omits the broader log-suppression changes from the source patch.
- `patches/0301-drm-panel-add-ayaneo-ar18-panel.patch`
  source: https://github.com/ROCKNIX/distribution/blob/aa418ad72e3e661b3834f46168bdf183276df2ac/projects/ROCKNIX/devices/SM8550/patches/linux/0064-gpu-drm-panel-add-ar16-4inch-panel.patch
  upstream: not submitted
  notes: Rewritten for the AYANEO Pocket MICRO 2 ST7123 panel on the mipi_dsi_multi_context API; timings and init sequence from the vendor device tree.
- `patches/0302-input-touchscreen-add-sitronix-st7123.patch`
  source: https://github.com/raspberrypi/linux/commit/6d4adb6bfea64581dff1c670a17333b63b8ba05d
  upstream: not submitted
  notes: Waveshare's Sitronix ST7123 driver from the Raspberry Pi kernel (rpi-6.18.y), with chip id 0x87 accepted for the AYANEO Pocket MICRO 2.
- `patches/0303-hid-add-ayaneo-pocket-micro2-force-feedback.patch`
  source: armada
  upstream: local
  notes: Rumble report format from the stock Android kernel's hid-ayaneo. Binds on every AYANEO 4001:0428 pad, rumble only on the Pocket MICRO 2.
- `patches/0304-ASoC-wcd938x-treat-failed-zdet-ramp-as-floating.patch`
  source: armada
  upstream: local
- `patches/0305-backlight-qcom-wled-always-disable-ovp-irq-at-probe.patch`
  source: armada
  upstream: local
- `patches/0026-dt-bindings-arm-qcom-ids-Add-SoC-ID-for-CQ8725S.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8750/patches/linux/0026-dt-bindings-arm-qcom-ids-Add-SoC-ID-for-CQ8725S.patch
  upstream: https://lore.kernel.org/r/20260605-cq8725s-soc-id-v1-1-bb1ef93de649@gmail.com
- `patches/0027-soc-qcom-socinfo-Add-CQ8725S-SoC-ID.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8750/patches/linux/0027-soc-qcom-socinfo-Add-CQ8725S-SoC-ID.patch
  upstream: https://lore.kernel.org/r/20260605-cq8725s-soc-id-v1-2-bb1ef93de649@gmail.com
- `patches/0742-dt-bindings-display-msm-Document-Adreno-830-GPU-GMU.patch`
  source: https://git.kernel.org/next/linux-next/c/ab20121e021588b634671958f7caa346bfa69621
  upstream: https://patch.msgid.link/20260809-pakala-gpu-v1-2-207ad1fac1c7@oss.qualcomm.com
  notes: 0742-0750 replace the ROCKNIX SM8750 GPU patches (0033, 0038, 0049) and Armada's 0038a and 0725. Upstream maps the GPU registers to `0x6d000` (covering RSCC), uses chip id 0x44050001 (Mesa 0002 matches it), reads the speed-bin fuse and places the GMU at `0x3d6c000`.
- `patches/0743-arm64-dts-qcom-sm8750-Add-GPU-clock-IOMMU-nodes.patch`
  source: https://git.kernel.org/next/linux-next/c/f695831a7af1f8d39203357572683981ebe4de77
  upstream: https://lore.kernel.org/r/20260714-gpucc_dt_v6-v6-1-16bf5289572d@oss.qualcomm.com
- `patches/0744-arm64-dts-qcom-sm8750-Add-GPU-and-GMU-nodes.patch`
  source: https://git.kernel.org/next/linux-next/c/9e39531ce39a98a77ddcf58f838a50dbf164092c
  upstream: https://patch.msgid.link/20260809-pakala-gpu-v1-3-207ad1fac1c7@oss.qualcomm.com
- `patches/0745-arm64-dts-qcom-sm8750-Add-GPU-cooling.patch`
  source: https://git.kernel.org/next/linux-next/c/c4dc1775c7723e9ed1ff74b649fe72d8aa741eb1
  upstream: https://patch.msgid.link/20260809-pakala-gpu-v1-4-207ad1fac1c7@oss.qualcomm.com
- `patches/0746-dt-bindings-clock-qcom-sm8750-gcc-Add-CX-power-domai.patch`
  source: https://git.kernel.org/next/linux-next/c/f9c74b6ed57922b1fdb1ed6835665e06b5ba01a5
  upstream: https://patch.msgid.link/20260924-qcom-tie-cx-to-gcc-v5-9-38732033e5b5@oss.qualcomm.com
- `patches/0747-clk-qcom-gcc-sm8750-Tie-the-CX-power-domain-to-contr.patch`
  source: https://git.kernel.org/next/linux-next/c/ff2531978f12b4727d79fd759f8c4b2ea2c63cf8
  upstream: https://patch.msgid.link/20260924-qcom-tie-cx-to-gcc-v5-26-38732033e5b5@oss.qualcomm.com
- `patches/0748-arm64-dts-qcom-sm8750-Add-GCC-CX-power-domain.patch`
  source: https://git.kernel.org/next/linux-next/c/ee35c132956f4797ed6be33c451decb94d1752af
  upstream: https://patch.msgid.link/20260924-qcom-tie-cx-to-gcc-v5-41-38732033e5b5@oss.qualcomm.com
- `patches/0035-arm64-dts-qcom-sm8750-set-CPU-capacity-dmips-mhz.patch`
  source: https://github.com/ROCKNIX/distribution/blob/f3e2b6187cd2ae2dc5122edfebe84228a314f2c5/projects/ROCKNIX/devices/SM8750/patches/linux/0076-arm64-dts-qcom-sm8750-set-CPU-capacity-dmips-mhz.patch
  upstream: unknown
- `patches/0037-arm64-dts-qcom-sm8750-add-CPU-thermal-cooling.patch`
  source: https://github.com/ROCKNIX/distribution/blob/b1e9d07b251c5a013d303a518106c547db001b74/projects/ROCKNIX/devices/SM8750/patches/linux/0075-arm64-dts-qcom-sm8750-add-CPU-thermal-cooling.patch
  upstream: unknown
  notes: Linux 7.2 supplies the CPU cooling-cell properties; Armada retains the missing passive trips and cooling maps.
- `patches/0542-arm64-dts-qcom-sm8750-describe-the-tcsr-download-mode-cookie.patch`
  source: armada
  upstream: local
- `patches/0557-arm64-dts-qcom-sm8750-add-the-soccp.patch`
  source: armada
  upstream: local
  notes: Companion DT for 0556: the SoCCP remoteproc, its SMP2P edge and the TCSR D-state register (needs the `tcsr` syscon from 0542). Enabled in the SoC file so every SM8750 board gets at least the fallback bus vote; a board sets `firmware-name` to get the reload.
- `patches/0749-drm-msm-a8xx-Add-support-for-Adreno-830-GPU.patch`
  source: https://git.kernel.org/next/linux-next/c/2c94d177a927a25d3eb111fe83694b5f84239069
  upstream: https://patch.msgid.link/20260809-pakala-gpu-v1-1-207ad1fac1c7@oss.qualcomm.com
- `patches/0750-drm-msm-a8xx-report-the-GMEM-size-of-the-active-slic.patch`
  source: https://git.kernel.org/next/linux-next/c/efbda69d92e6a4822c5f2d09910f547872a9498d
  upstream: https://patch.msgid.link/20260930183840.1171-1-theflyingrahul@gmail.com
- `patches/0039-wifi-ath12k-add-initial-hardware-definition-for-WCN7.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8750/patches/linux/0039-wifi-ath12k-add-initial-hardware-definition-for-WCN7.patch
  upstream: unknown
  notes: Armada refreshed only the hardware-parameter insertion context for Linux 7.2's expanded IPQ5332 entry; WCN7860 behavior is unchanged.
- `patches/0040-wifi-ath12k-send-QDSS-config-when-CNSS_QDSS_CFG_MISS.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8750/patches/linux/0040-wifi-ath12k-send-QDSS-config-when-CNSS_QDSS_CFG_MISS.patch
  upstream: unknown
- `patches/0041-wifi-ath12k-disable-CNSS_QDSS_CFG_MISS_V01-for-the-W.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8750/patches/linux/0041-wifi-ath12k-disable-CNSS_QDSS_CFG_MISS_V01-for-the-W.patch
  upstream: unknown
- `patches/0042-PCI-pwrctrl-pwrseq-add-support-for-WCN7860.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8750/patches/linux/0042-PCI-pwrctrl-pwrseq-add-support-for-WCN7860.patch
  upstream: unknown
- `patches/0043-power-sequencing-qcom-wcn-add-support-for-WCN7860.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8750/patches/linux/0043-power-sequencing-qcom-wcn-add-support-for-WCN7860.patch
  upstream: unknown
- `patches/0045-Bluetooth-qca-add-WCN7860-support.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8750/patches/linux/0045-Bluetooth-qca-add-WCN7860-support.patch
  upstream: unknown
  notes: Armada rebased ROCKNIX's WCN7860 additions onto Linux 7.1 after upstream restructured the QCA Bluetooth switch cases and renamed the power-off helper.
- `patches/0066-scsi-ufs-ufs-qcom-add-sm8750-compatible.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8750/patches/linux/0066-scsi-ufs-ufs-qcom-add-sm8750-compatible.patch
  upstream: unknown
- `patches/0509-soc-qcom-pmic_glink_altmode-defer-until-mux-switch-ready.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8750/patches/linux/0509-soc-qcom-pmic_glink_altmode-defer-until-mux-switch-ready.patch
  upstream: unknown
  notes: Armada gates both deferrals on `qcom,sm8750`. ROCKNIX runs this only in its SM8750 kernel, where the mode-switch supplier registers late. Boards that declare no mode-switch at all (the AYANEO SM8550 family) would defer forever, which blocks the DP aux bridges, keeps the msm DRM aggregate from binding, and leaves the internal panel dark. Hardware-confirmed on the Pocket EVO. In Linux 7.2.6, a declared-but-late provider already returns `-EPROBE_DEFER` through the `IS_ERR()` path ahead of these NULL checks, so the gated checks are ROCKNIX's SM8750 fallback on top of that distinction rather than the primary defer mechanism.
- `patches/0519-usb-typec-ucsi-clear-USB-role.patch`
  source: https://github.com/ROCKNIX/distribution/commit/c9629c95a5655dcfb68e8f3aaf75f9967a9e9656
  upstream: unknown
- `patches/0517-usb-typec-mux-dont-swallow-EPROBE_DEFER.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8750/patches/linux/0517-usb-typec-mux-dont-swallow-EPROBE_DEFER.patch
  upstream: unknown
  notes: Retains only array initialization; Linux 7.2.6 includes the probe-deferral fixes.
- `patches/0603-ASoC-codecs-wcd939x-keep-the-codec-resumed-while-a-ja.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8750/patches/linux/0603-ASoC-codecs-wcd939x-keep-the-codec-resumed-while-a-ja.patch
  upstream: unknown
  notes: Armada holds only the TX SoundWire device (the source held RX and TX). MBHC reports through TX; the RX link suspends and is resumed on demand for impedance detection. Releasing TX as well loses plug events because the in-band wake from clock stop never raises swr_wake_irq on SM8750.
- `patches/0072-ASoC-lpass-rx-macro-add-HPH-PCM-mode.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8750/patches/linux/0072-ASoC-lpass-rx-macro-add-HPH-PCM-mode.patch
  upstream: unknown
- `patches/0073-ASoC-wcd939x-add-HPH-PCM-HiFi-mode.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8750/patches/linux/0073-ASoC-wcd939x-add-HPH-PCM-HiFi-mode.patch
  upstream: unknown
  notes: Armada keeps the HPH PCM remap off the TX device, whose channel ids overlap the HPH ones, and writes the crosstalk coefficients before the compander-off return.
- `patches/0081-ASoC-wcd939x-fix-headphone-analog-volume-controls.patch`
  source: armada
  upstream: local
- `patches/0074-soundwire-qcom-PCM-data-port-format-enable.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8750/patches/linux/0074-soundwire-qcom-PCM-data-port-format-enable.patch
  upstream: unknown
- `patches/0075-ASoC-wsa884x-preserve-Pocket-S2-compander-gain.patch`
  source: armada
  upstream: local
  notes: AYANEO Pocket S2, Pocket DS and KONKR Pocket FIT fix. The WSA884x amplifier's POST_PMU sequence selects the SoundWire compander, but the unmute path immediately overrode it with the fixed CSR gain, discarding the boards' matched compander plus digital-volume configuration. The driver now keeps the compander selection when its port is enabled, gated on the `ayaneo,pocket-s2`, `ayaneo,pocketds` and `konkr,pocket-fit` machine compatibles, so every other WSA884x machine keeps the original fixed-gain behavior. This requires a matching UCM that enables both macro companders, initializes both PA controls to 17 (hardware gain index 14, unity), and uses digital volume. Scoped to the Armada distribution; not a Linux upstream submission.
- `patches/0612-ROCKNIX-odin3-q6apm-start-mi2s-port-at-prepare.patch`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8550/patches/linux/0612-ROCKNIX-odin3-q6apm-start-mi2s-port-at-prepare.patch
  upstream: unknown
- `patches/0613-ASoC-q6apm-scope-prepare-start-to-MI2S.patch`
  source: armada
  upstream: local
  notes: Armada added this follow-up to limit `0612` to playback MI2S DAIs; without it, the ROCKNIX change would affect every playback DAI using the shared q6apm driver.
- `patches/0528-ASoC-qcom-sc8280xp-suspend-the-card-and-its-streams.patch`
  source: armada
  upstream: local
- `patches/0538-ASoC-qcom-sc8280xp-cap-Pocket-DS-speaker-digital-volume.patch`
  source: armada
  upstream: local
  notes: AYANEO Pocket DS only. With the compander speaker path from `0075`, the speakers audibly distorted at WSA RX digital volume 73 and were clean at 71 across the bass, hot-master and vocal test clips, so the upstream limit of 81 is lowered to 71 on this board. A peak limiter in userspace could allow a higher cap later.
- `patches/0529-ASoC-qdsp6-q6apm-fail-the-graph-open-when-the-DSP-rejects-it.patch`
  source: armada
  upstream: local
- `patches/0530-ASoC-qdsp6-release-AudioReach-graphs-across-system-suspend.patch`
  source: armada
  upstream: local
- `patches/0531-ASoC-qcom-sc8280xp-release-the-board-i2s-clock-across-system-suspend.patch`
  source: armada
  upstream: local
  notes: A PCM still open at suspend (on the Odin 3, the power key's UI sound) kept the q6prm "i2s_clk" enabled, so the ADSP's AUDIO DRV blocked CX power collapse for the whole sleep. The card now drops the clock in suspend_post and restores it in resume_pre.
- `patches/0532-hwmon-pwm-fan-optionally-run-the-fan-while-charging-in-s2idle.patch`
  source: armada
  upstream: local
- `patches/0540-arm64-signal-reapply-the-ssbs-policy-on-sigreturn.patch`
  source: armada
  upstream: local
- `patches/0619-drm-msm-map-submitqueue-priority-onto-high-low.patch`
  source: armada
  upstream: local
- `patches/0620-drm-msm-a6xx-hfi-irq-clears-only-the-cm3-fault.patch`
  source: https://github.com/kettlelinux/kettlelinux/blob/d379ae1d0efeb8dd282647a1598efd719c6ecd4d/kernel/patches/40-kettle/1350-drm-msm-a6xx-hfi-irq-clears-only-the-cm3-fault.patch
  upstream: unknown
- `patches/0621-drm-msm-a6xx-bound-the-gmu-wait-for-a-fault-devcoredump.patch`
  source: https://github.com/kettlelinux/kettlelinux/blob/d379ae1d0efeb8dd282647a1598efd719c6ecd4d/kernel/patches/40-kettle/1351-drm-msm-a6xx-bound-the-gmu-wait-for-a-fault-devcoredump.patch
  upstream: unknown
- `patches/0622-drm-msm-a6xx-mask-the-hfi-interrupt-before-booting-the-gmu.patch`
  source: armada
  upstream: local
- `patches/0623-arm64-dts-qcom-sm8550-sm8650-add-the-ADSP-FastRPC-remote-heap.patch`
  source: https://github.com/hashtagbasit/SteamOS-ARM-Port/blob/162a3d97e61d94e0740193a8af49fc95de408439/external-and-mods/kernel-sm8550/dts/qcs8550-ayn-odin2-gyro.dtsi
  upstream: not submitted
  notes: justjoseorg's heap node, memory-region and qcom,vmids, moved from a board file into the SM8550, QCS8550 and SM8650 SoC dtsi so every board on those SoCs has them; qcom,fastrpc-adsp-sensors-pdr is dropped because this kernel does not read it.
- `dts/qcs8550-ayaneo-pocketace.dts`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8550/linux/dts/qcom/qcs8550-ayaneo-pocketace.dts
- `dts/qcs8550-ayaneo-pocket-common.dtsi`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8550/linux/dts/qcom/qcs8550-ayaneo-pocket-common.dtsi
- `dts/qcs8550-ayaneo-pocketdmg.dts`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8550/linux/dts/qcom/qcs8550-ayaneo-pocketdmg.dts
- `dts/qcs8550-ayaneo-pocketds.dts`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8550/linux/dts/qcom/qcs8550-ayaneo-pocketds.dts
- `dts/qcs8550-ayaneo-pocketevo.dts`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8550/linux/dts/qcom/qcs8550-ayaneo-pocketevo.dts
- `dts/qcs8550-ayaneo-pockets1k.dts`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8550/linux/dts/qcom/qcs8550-ayaneo-pockets1k.dts
- `dts/qcs8550-ayaneo-pockets2k.dts`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8550/linux/dts/qcom/qcs8550-ayaneo-pockets2k.dts
- `dts/qcs8550-ayn-common.dtsi`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8550/linux/dts/qcom/qcs8550-ayn-common.dtsi
- `dts/qcs8550-ayn-odin2.dts`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8550/linux/dts/qcom/qcs8550-ayn-odin2.dts
- `dts/qcs8550-ayn-odin2mini.dts`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8550/linux/dts/qcom/qcs8550-ayn-odin2mini.dts
- `dts/qcs8550-ayn-odin2portal.dts`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8550/linux/dts/qcom/qcs8550-ayn-odin2portal.dts
- `dts/qcs8550-ayn-thor.dts`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8550/linux/dts/qcom/qcs8550-ayn-thor.dts
- `dts/qcs8550-retroidpocket-rp6.dts`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8550/linux/dts/qcom/qcs8550-retroidpocket-rp6.dts
- `dts/qcs8550-retroidpocket-rp6-top-dpad.dts`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8550/linux/dts/qcom/qcs8550-retroidpocket-rp6-top-dpad.dts
- `dts/qcs8550-retroidpocket-rpnova.dts`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8550/linux/dts/qcom/qcs8550-retroidpocket-rpnova.dts
- `dts/sm8650-ayaneo-common.dtsi`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8650/linux/dts/qcom/sm8650-ayaneo-common.dtsi
- `dts/sm8650-ayaneo-ps2.dts`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8650/linux/dts/qcom/sm8650-ayaneo-ps2.dts
- `dts/sm8650-konkr-pf.dts`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8650/linux/dts/qcom/sm8650-konkr-pf.dts
- `dts/sm8250-retroidpocket-common.dtsi`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8250/linux/dts/qcom/sm8250-retroidpocket-common.dtsi
- `dts/sm8250-ayaneo-pocket-micro2.dts`
  source: armada
  notes: Board file for the AYANEO Pocket MICRO 2; fan is left to armada-powerd (no thermal-zone include).
- `dts/sm8250-ayn-thorlite.dts`
  source: https://github.com/ROCKNIX/distribution/blob/dbea089dd83e156babbbcabc677117cef08f1148/projects/ROCKNIX/devices/SM8250/linux/dts/qcom/sm8250-ayn-thorlite.dts
  notes: Imported verbatim from ROCKNIX; SHA-256 `62a06545c46fe052c69699c20c8c6b330c4b64a3ecdb6b5ba99420868a78597d`. Authored by Philippe Simons; retains the original BSD-3-Clause SPDX identifier and Retroid Pocket copyright notice.
- `dts/sm8250-ayn-thorlite.dts.patch`
  source: armada
  notes: Armada removes the kernel touchscreen coordinate transforms after copying `dts/sm8250-ayn-thorlite.dts`; Gamescope/libinput maps the native digitizer coordinates to the rotated outputs, and applying both transforms makes the right edge behave as the top edge. This matches Armada's full Thor handling. Also enables the AYN button.
- `dts/sm8250-mangmi-air-y-pro.dts`
  source: https://github.com/ROCKNIX/distribution/blob/807c74fc46c124891d8aa9b57a68533d38e9a6b2/projects/ROCKNIX/devices/SM8250/linux/dts/qcom/sm8250-mangmi-air-y-pro.dts
  notes: Imported verbatim from ROCKNIX; SHA-256 `d98f1104f4fe29f9bf8c94692beb491e840332a851f1f6994f015973ba24c018`.
- `dts/sm8250-mangmi-air-y-pro.dts.patch`
  source: armada
  notes: Exposes the two centre-logo RGB LEDs on left AW20036 channels 24–29, verified on Air Y Pro hardware.
- `dts/sm8250-mangmi-pocket-max.dts`
  source: https://github.com/ROCKNIX/distribution/blob/807c74fc46c124891d8aa9b57a68533d38e9a6b2/projects/ROCKNIX/devices/SM8250/linux/dts/qcom/sm8250-mangmi-pocket-max.dts
  notes: Imported verbatim from ROCKNIX; SHA-256 `f6128a97cf510fcd9ecf568a2e512c3f6f4210ad43e4fb1f542740f4b140dfd2`.
- `dts/sm8250-mangmi-pocket-max.dts.patch`
  source: armada
  notes: Drops ROCKNIX's kernel thermal-zone fan include after copying the DTS; Armada powerd owns the PWM fan curve and must not race a second controller.
- `dts/sm8250-retroidpocket-flip2.dts`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8250/linux/dts/qcom/sm8250-retroidpocket-flip2.dts
- `dts/sm8250-retroidpocket-flip2-visionox.dts`
  source: armada
  notes: Support for Visionox display panel models
- `dts/sm8250-retroidpocket-rp5.dts`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8250/linux/dts/qcom/sm8250-retroidpocket-rp5.dts
- `dts/sm8250-retroidpocket-rp5-visionox.dts`
  source: armada
  notes: Support for Visionox display panel models
- `dts/sm8250-retroidpocket-rpmini.dts`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8250/linux/dts/qcom/sm8250-retroidpocket-rpmini.dts
- `dts/sm8250-retroidpocket-rpminiv2.dts`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8250/linux/dts/qcom/sm8250-retroidpocket-rpminiv2.dts
- `dts/sm8750-konkr-pf-elite.dts`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8750/linux/dts/qcom/sm8750-konkr-pf-elite.dts
- `dts/sm8750-konkr-pf-elite.dts.patch`
  source: armada
  notes: Armada adapts the Elite touchscreen node to the full ROCKNIX Chipone fork shared with the SM8650 Pocket FIT, keeps volume-up from waking the system, and adds the DisplayPort playback link required for USB-C DP Alt Mode audio; the touchscreen driver is selected only by those two device-tree nodes. Armada also marks PCIe WAKE# active-low and idles the codec rails in LPM during s2idle, and points the SoCCP remoteproc at the Elite's own firmware.
- `dts/cq8725s-ayn-common.dtsi`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8750/patches/linux/0046-arm64-dts-qcom-Add-AYN-CQ8725S-Common.patch
  notes: Armada extracted this DTS from the cited ROCKNIX patch and then applied later ROCKNIX DTS updates, including the Odin 3 haptics nodes from ROCKNIX commit `81a31e3d0f`.
- `dts/cq8725s-ayn-odin3.dts`
  source: https://github.com/ROCKNIX/distribution/blob/bcf3b5bc574990b96543484575b06f912153a715/projects/ROCKNIX/devices/SM8750/patches/linux/0047-arm64-dts-qcom-Add-AYN-Odin3.patch
  notes: Armada extracted this DTS from the cited ROCKNIX patch and then applied later ROCKNIX DTS updates.
- `dts/cq8725s-ayn-odin3.dts.patch`
  source: armada
  notes: Armada enables DPU dithering, codec-rail LPM sleep states, the PM8550 RGB charge LED and the WCD DMIC internal mic route after copying `dts/cq8725s-ayn-odin3.dts`.
- `dts/cq8725s-ayn-common.dtsi.patch`
  source: armada
  notes: Armada keeps volume-up from waking the system, marks Odin 3's RSInput node as connected to the Qualcomm haptics device, supplies the device's 1024 range, marks PCIe WAKE# active-low, and keeps the four switched WCN7860 PMU supply rails always-on because re-enabling them at resume can hang the SoC. The 70-count `axis-deadzone` (an unmeasured ROCKNIX bring-up value) was dropped; like the RP6 and every other RSInput device the Odin 3 now passes its stick value through, leaving deadzone policy to Steam Input and the game.
- `dts/qcs8550-ayaneo-pocket-common.dtsi.patch`
  source: armada
  notes: Armada keeps volume-up from waking the system, removes the SDHCI capability mask, marks PCIe WAKE# active-low, and idles the codec rail in LPM during s2idle after copying `dts/qcs8550-ayaneo-pocket-common.dtsi`.
- `dts/qcs8550-ayaneo-pocketace.dts.patch`
  source: armada
  notes: Armada applies this local patch after copying `dts/qcs8550-ayaneo-pocketace.dts`.
- `dts/qcs8550-ayaneo-pocketdmg.dts.patch`
  source: armada
  notes: Armada applies this local patch after copying `dts/qcs8550-ayaneo-pocketdmg.dts`.
- `dts/qcs8550-ayaneo-pockets1k.dts.patch`
  source: armada
  notes: Armada applies this local patch after copying `dts/qcs8550-ayaneo-pockets1k.dts`.
- `dts/qcs8550-ayaneo-pockets2k.dts.patch`
  source: armada
  notes: Armada applies this local patch after copying `dts/qcs8550-ayaneo-pockets2k.dts`.
- `dts/qcs8550-ayaneo-pocketds.dts.patch`
  source: armada
  notes: Armada applies this local patch after copying `dts/qcs8550-ayaneo-pocketds.dts`. It labels the lower GT911 input device as `bottom_touchscreen` and moves the lower panel onto the ST7703 driver contract: `vcc-supply` for the SGM3804 charge pump, and the former `enable-gpio` on TCA6408 GPIO0 re-modeled as a fixed regulator consumed as `iovcc-supply`. It also declares `vin-supply = <&tca6424_vcc>` on both expander-switched fixed regulators (`vdd_ts`, `panel1-iovcc`): the pca953x suspend callback disables its own VCC, and without the vin link the regulator core would cut the expander while the GT911 still holds VDDIO enabled, aborting async deep suspend mid Goodix screen-off write. It also adds a `gpio-keys-lid` node for the hinge hall sensor: stock Android reads it as a ROHM BU52053NVx (`qti.sensor.hall_effect`) through the SLPI sensor HAL rather than any Linux input driver, with no devicetree node of its own — its GPIO (TLMM 166, active-low, no internal pull; confirmed live via `/sys/kernel/debug/gpio` while toggling the lid) came from `dri_irq_num` in the vendor's `/vendor/etc/sensors/config/kailua_bu52053nvx_0.json` on-device.
- `dts/qcs8550-ayaneo-pocketevo.dts.patch`
  source: armada
  notes: Armada keeps the AYA Space, Menu, LC, and RC auxiliary keys from waking the system.
- `dts/qcs8550-ayn-common.dtsi.patch`
  source: armada
  notes: Armada keeps volume-up from waking the system, removes the SDHCI capability mask, and marks the shared RSInput node as connected to the PM8550B haptics device declared in the same common tree; this covers the AYN and Retroid products that inherit both nodes, including Pocket 6 and Nova. Armada also marks PCIe WAKE# active-low, idles the codec rails in LPM during s2idle, and powers RSInput from `vdd_mcu_3v3` instead of the shared `vreg_bob2`, without always-on, so the driver can cut the MCU in suspend.
- `dts/qcs8550-ayn-odin2.dts.patch`
  source: armada
  upstream: local
- `dts/qcs8550-ayn-odin2portal.dts.patch`
  source: armada
  notes: Adds the back buttons from the Odin 2 DTS into the Odin 2 Portal DTS
- `dts/qcs8550-retroidpocket-rp6.dts.patch`
  source: armada
  notes: Armada switches Pocket 6 from ROCKNIX's Odin 2 fallback to audio firmware extracted from a Pocket 6 vendor image, and drives its haptics actuator as an LRA with the stock Android values (board-id 0x1001f overlay) instead of the inherited Odin 2 ERM config.
- `dts/qcs8550-retroidpocket-rpnova.dts.patch`
  source: armada
  reference: https://github.com/RetroidPocket/linux/blob/2209a42da1a891d0d140293f5831c50e4aa9cc61/arch/arm64/boot/dts/qcom/qcs8550-retroidpocket-rpnova.dts
  notes: Armada disables the inherited Pocket 6 PWM backlight and removes its panel reference so Nova uses its panel driver’s DSI backlight. Matches Retroid’s Nova panel wiring: L11B/L12B/L13B for vdd/vddio/vci, GPIO 70/143 fixed regulators for vdd18/vdd28, and rotation 0. Removes the inherited avdd supply and retains Armada DPU dithering and Nova's own ADSP firmware. The ROCKNIX Nova → RP6 → AYN common inheritance remains unchanged for other systems.
- `dts/qcs8550-ayn-thor.dts.patch`
  source: armada
  notes: Armada fixes the hall-sensor pinctrl, makes only the lid-open edge wake, corrects touch orientation, and enables DPU dithering on the top panel after copying `dts/qcs8550-ayn-thor.dts`.
- `dts/sm8650-ayaneo-common.dtsi.patch`
  source: armada
  notes: Armada keeps volume-up from waking the system, wires the upstream SY7758 driver, marks PCIe WAKE# active-low, idles the codec rails in LPM during s2idle, and keeps the RTC offset in an SDAM cell with the alarm enabled after copying `dts/sm8650-ayaneo-common.dtsi`.
- `dts/sm8650-ayaneo-ps2.dts.patch`
  source: armada
  notes: Armada selects the accepted Pocket S2 WSA2 sound-card mapping after copying the ROCKNIX DTS.
- `dts/sm8650-konkr-pf.dts.patch`
  source: armada
  notes: Armada selects the shared WSA2 channel mapping through a Pocket FIT-specific sound-card compatible and binds `konkr_sysbtn` to the controller MCU UART, and loads its own ADSP firmware.

- `patches/0505-arm64-emulate-unaligned-atomics.patch`
  source: https://github.com/bylaws/linux/commit/7ae989a43ae7e3cb8007ac21c28dacc24c9d8320
  upstream: unknown
  notes: Rebased patch context for Linux 7.2.3 and Armada's compat-input patch; the unaligned-atomic handler is unchanged.
- `patches/0505a-arm64-unaligned-atomics-cover-the-load128-store-exclusive.patch`
  source: armada
  upstream: local
- `patches/0563-ASoC-codecs-lpass-macro-force-runtime-suspend-across-system-sleep.patch`
  source: armada
  upstream: local
  notes: The macros stay runtime-active through s2idle while SoundWire is held; force-suspend so the ADSP (the "AUDIO" CXPC voter) can release LPASS.
- `patches/0080-ASoC-codecs-lpass-tx-macro-track-every-active-decimator.patch`
  source: armada
  upstream: local
- `patches/0564-soundwire-qcom-force-runtime-suspend-across-system-sleep.patch`
  source: armada
  upstream: local
  notes: Same for the SoundWire controller; the WCD9390 peripherals are kept runtime-active for jack detection.
- `patches/0565-pinctrl-qcom-sm8650-lpass-lpi-force-runtime-suspend-across-system-sleep.patch`
  source: armada
  upstream: local
  notes: Same for the LPASS LPI pin controller, which the SoundWire controllers keep runtime-active through their device links (held by 0603); otherwise it keeps LPASS_HW_MACRO/DCODEC voted in s2idle.
- `patches/0570-pmdomain-core-Rename-genpd_status_on.patch`
  source: https://git.kernel.org/next/linux-next/c/81f1099186fd501768ea4bd24523347211322fbe
  upstream: n/a
  notes: Prerequisite for 0573.
- `patches/0571-pmdomain-core-Allow-a-non-CPU-device-in-a-CPU-PM-dom.patch`
  source: https://git.kernel.org/next/linux-next/c/9e8dff8e097814e4d7c65cd211ccb1e2fceb460a
  upstream: https://lore.kernel.org/all/CAPx+jO-sCierYj8jnoKQHckJG16dOBxnNrsZVYO=38R2cLV8nw@mail.gmail.com/
  notes: Prerequisite for 0573.
- `patches/0572-pmdomain-core-Add-a-genpd-config-to-support-unknown-.patch`
  source: https://git.kernel.org/next/linux-next/c/2224d686e788d6ad3af4cc48bbf68723f8abd326
  upstream: https://lore.kernel.org/all/20260811-domain_off_ss3-v1-0-6a0a0fc023f5@oss.qualcomm.com/
  notes: Prerequisite for 0573 (GENPD_FLAG_POWER_UNKNOWN).
- `patches/0573-cpuidle-psci-Initialize-the-PM-domains-in-powered-of.patch`
  source: https://git.kernel.org/next/linux-next/c/6d3080bfe007c88c38b6faf6d3ab23171af359f0
  upstream: https://lore.kernel.org/all/20260811-domain_off_ss3-v1-0-6a0a0fc023f5@oss.qualcomm.com/
  notes: SM8750 uses PSCI OS-initiated mode; the CPU cluster genpds were registered as on, which can pick a shallower domain idle state.
- `patches/0574-cpuidle-psci-Move-initialization-a-bit-earlier-in-th.patch`
  source: https://git.kernel.org/next/linux-next/c/65705b18162bbf0771adf742ee528521957fb496
  upstream: n/a
  notes: Second half of the OSI init fix.
- `patches/0575-thermal-drivers-qcom-spmi-temp-alarm-Fix-temp_map-in.patch`
  source: https://git.kernel.org/next/linux-next/c/1419c8256fba229625ec7dbd465d39b6b90dab2c
  upstream: https://patch.msgid.link/20260928132823.1426513-1-djakov@kernel.org
  notes: Out-of-bounds read of the trip table; wrong PMIC temp-alarm thresholds whenever the threshold index is non-zero (PM8550/PMIH0108 on the Odin 3).
- `patches/0576-wifi-ath12k-fix-out-of-bounds-access-on-TX-stats-arr.patch`
  source: https://git.kernel.org/next/linux-next/c/c8f83d3389d1d1b318ac3bd2ae3d60c2862c90b4
  upstream: https://patch.msgid.link/20260819053247.1420393-2-pardeep.kaur@oss.qualcomm.com
  notes: Unchecked hardware indices on the TX completion path could write past the stats arrays.
- `patches/0577-wifi-ath12k-Reserve-space-for-a-string-terminator.patch`
  source: https://git.kernel.org/next/linux-next/c/13b15eabe2c541b80406166964cdc8ccb5e9c32a
  upstream: https://patch.msgid.link/20261003095913.575108-1-yaojiale02@163.com
  notes: ath12k string buffer missing room for the NUL.
- `patches/0578-wifi-ath12k-Free-allocated-CE-IRQs-on-request_irq-fa.patch`
  source: https://git.kernel.org/next/linux-next/c/12ca935af2e68447e9218a615ebbb5ff7faf1554
  upstream: https://patch.msgid.link/20260819110215.2485514-2-aaradhana.sahu@oss.qualcomm.com
  notes: Error-path cleanup for CE IRQ registration.
- `patches/0579-drm-msm-dpu-compute-the-CRTC-bandwidth-from-the-stat.patch`
  source: https://git.kernel.org/next/linux-next/c/480ba24aa34031c898d0a711405664cd947bbee4
  upstream: https://patch.msgid.link/20261002130656.50577-1-26rote@gmail.com
  notes: After DPMS off/on or s2idle the MDP average bandwidth vote stayed 0 until a plane changed.
- `patches/0555-soc-qcom-aoss-add-a-raw-qmp-send-debugfs-file.patch`
  source: armada
  upstream: local
  notes: Debug only. /sys/kernel/debug/qcom_aoss/send forwards a raw QMP message, used to start the AOP lpm_mon violator log (read back from 0xc320000) that shows which DRV blocks CX power collapse in suspend.
- `patches/0556-remoteproc-qcom-pas-manage-the-sm8750-soccp.patch`
  source: armada
  upstream: local
  notes: Fixes the SM8750 s2idle wake hang at its cause and replaces the SN4 sleep keepalive (and the 0521 PCIe suspend OPP floor before it). The bootloader's early SoCCP image sits in D0 behind the system NoC with no bus vote; the driver reloads soccp.mbn, which parks itself in D3, and the SoC then also reaches CX shutdown and DDR low power in suspend. Until the TCSR D-state register shows D3 the driver holds the SoCCP's path to DDR itself, so a board without soccp.mbn still wakes, without the deeper sleep. Odin 3 firmware: `qcom/sm8750/ayn/odin3/soccp.mbn`, from the device's modem partition.
- `patches/0561-soc-qcom-override-the-sm8750-pcie-state-manager-power-control.patch`
  source: armada
  upstream: local
  notes: The SM8750 PCIe state managers (CESTA) report a power state to the AOSS. Downstream pci-msm sets their PWR_CTRL/PWR_CTRL_MASK override at init and only clears it once it runs the state manager program, which pcie-qcom never does; without the override the PCI0_CESTA requestor stays busy in suspend and blocks AOSS deep sleep. Set once at boot on SM8750.
- `patches/0566-soc-qcom-hand-the-sm8750-mdss-to-the-display-sequencer-at-suspend.patch`
  source: armada
  upstream: local
  notes: The display RSC/CESTA keeps reporting the display active (DISPLAY requestor busy, no AOSS deep sleep) until its CRM software client releases its pass-through votes with the MDSS GDSC under hardware control; then the sequencer collapses the GDSC itself ("mode2"). Replays the downstream display-off handoff at system suspend (after the MDSS, MMCX held) and wakes the sequencer again on resume before msm. Bound by an `armada,sm8750-disp-cesta` node (Odin 3 DTS). With 0561, the Odin 3 reaches AOSS deep sleep for all of s2idle. Writing pass-through votes with the display running stalls the CRM and hangs the next CX collapse, so they are only written with the display suspended.
- `patches/0700-wifi-mac80211-fix-unauthorised-port-check-for-encap-.patch`
  source: https://git.kernel.org/next/linux-next/c/d59b9bf7df49367e01b06e82dd0f6e7ad3be493c
  upstream: https://patch.msgid.link/20260802105818.dd5da579813d.I51ed0121154bb652bebc97bb0597b1fae9ac978f@changeid
- `patches/0701-wifi-mac80211-fix-key-selection-for-encap-offload-fr.patch`
  source: https://git.kernel.org/next/linux-next/c/0e80db08668b560b3522849cb705623148bcd4b5
  upstream: https://patch.msgid.link/20260802105818.0feb7ad61047.Ia506ca211176a3c466bc60e4cc3e506df34a4a67@changeid
- `patches/0702-wifi-mac80211-don-t-send-encap-offload-frames-unencr.patch`
  source: https://git.kernel.org/next/linux-next/c/a48daf145fed445d41ef422573411500785415c8
  upstream: https://patch.msgid.link/20260802085818.1336616-7-johannes@sipsolutions.net
  notes: ath12k uses 802.11 encapsulation offload; without this, mac80211 can send data frames unencrypted to a station that requires encryption.
- `patches/0703-wifi-mac80211-drop-encap-offload-frames-with-a-taint.patch`
  source: https://git.kernel.org/next/linux-next/c/c8ddbe1e8c43f6d008591c50f8be8de39cdce267
  upstream: https://patch.msgid.link/20260802105818.870b6ef31374.Ib87175b55b9fd94c16ba6d9cd816b7a09248df87@changeid
- `patches/0704-mac80211-tx-Use-info-flags-in-ieee80211_tx_h_select_.patch`
  source: https://git.kernel.org/next/linux-next/c/5f2530a4df8e0573e54cc0f4175c06ecb810a4dd
  upstream: https://patch.msgid.link/20260908094341.12196-1-spasswolf@web.de
- `patches/0705-wifi-mac80211-don-t-reset-the-TXQ-scheduling-round-n.patch`
  source: https://git.kernel.org/next/linux-next/c/8ea81827d3537db7cfcc82c008f052bb1bbe7567
  upstream: https://patch.msgid.link/20260908144155.756569-1-julius@bairaktaris.de
- `patches/0708-wifi-ath12k-fix-truncated-TX-buffer-DMA-address-in-M.patch`
  source: https://git.kernel.org/next/linux-next/c/979ecb88ed3528e08dd7f87b90b029374226ca84
  upstream: https://patch.msgid.link/20260818-ath12k-truncated-tx-dma-addr-v1-1-ead978969371@oss.qualcomm.com
  notes: TX buffers mapped above 4 GB were handed to the firmware with the high address bits cleared.
- `patches/0709-wifi-ath12k-fix-stale-skb-pointers-after-aligned-TX-.patch`
  source: https://git.kernel.org/next/linux-next/c/6c40719489c8d799798989b15bc07b0700c132f8
  upstream: https://patch.msgid.link/20260818-ath12k-uaf-for-aligned-tx-v1-1-d6ae195b15e7@oss.qualcomm.com
- `patches/0710-wifi-ath12k-fix-DMA-unwind-for-ext-MSDU-descriptor-r.patch`
  source: https://git.kernel.org/next/linux-next/c/4de5a8a0edddc453f1a4c93b6d9f09013a23b72e
  upstream: https://patch.msgid.link/20260813-ext-msdu-fix-v1-1-c5e80ccd061a@oss.qualcomm.com
- `patches/0711-wifi-ath12k-signal-regd-update-completion-when-reg-e.patch`
  source: https://git.kernel.org/next/linux-next/c/f2576dc0f894ef33045ba7ed057ec417988bba8a
  upstream: https://patch.msgid.link/20260729-ath12k-regd-wait-timeout-v1-1-504aa6e7e93c@oss.qualcomm.com
- `patches/0712-soc-qcom-pmic_glink-Avoid-losing-early-rpmsg-probe.patch`
  source: https://git.kernel.org/next/linux-next/c/1517efff0e9d21cc4c9cc7ffa1fcc30225e6b069
  upstream: https://patch.msgid.link/20260720-topic-pmic_glink_defer-v1-1-94c0f233f2f7@oss.qualcomm.com
  notes: If the rpmsg device appears before pmic_glink has probed, USB-C and battery reporting were lost for that boot.
- `patches/0713-soc-qcom-pmic_glink-Fix-device-access-from-worker-du.patch`
  source: https://git.kernel.org/next/linux-next/c/7d0767c5cd878707fd6711023731549c83563840
  upstream: https://lore.kernel.org/r/20260819-b4-soc-qcom-pmic-glink-fix-device-access-on-worker-while-suspended-v3-1-169b00e0d9d4@oss.qualcomm.com
- `patches/0714-drm-msm-Fix-vm_bo-use-after-free-in-with_vm_locks.patch`
  source: https://git.kernel.org/next/linux-next/c/81878aa1a2f551f51a3d3aef2a9509503ec34d8b
  upstream: https://lore.kernel.org/r/20260916175548.2089821-1-vulab@iscas.ac.cn
- `patches/0716-clk-qcom-rcg2-Initialize-shared-floor-clock-state.patch`
  source: https://git.kernel.org/next/linux-next/c/b9a14395e6edfeb3ce241f19f84991106efcd3b3
  upstream: https://patch.msgid.link/20260917-topic-qc_clk_fixes-v1-1-5531cb00514b@oss.qualcomm.com
- `patches/0717-clk-qcom-rcg2-Clear-force-enable-after-rate-failure.patch`
  source: https://git.kernel.org/next/linux-next/c/ae881bdb1b1d081ea3febcc16fe6ee16d3a2a0d1
  upstream: https://patch.msgid.link/20260917-topic-qc_clk_fixes-v1-3-5531cb00514b@oss.qualcomm.com
- `patches/0718-clk-qcom-rcg2-Propagate-force-enable-status-errors.patch`
  source: https://git.kernel.org/next/linux-next/c/396e900a120db686c3fe375df3b9fb6a62f173a6
  upstream: https://patch.msgid.link/20260917-topic-qc_clk_fixes-v1-2-5531cb00514b@oss.qualcomm.com
- `patches/0719-firmware-qcom_scm-handle-empty-PAS-resource-table.patch`
  source: https://git.kernel.org/next/linux-next/c/abb698e1a973869a3f82a604d5ef7c6066f60725
  upstream: https://patch.msgid.link/20260921195636.1925869-2-mukesh.ojha@oss.qualcomm.com
- `patches/0722-drm-msm-a6xx-Honor-perfmode_bw-threshold-on-A8x.patch`
  source: https://git.kernel.org/next/linux-next/c/db6a2e4a7ebd4378d03a97f4bef22f8c157240ad
  upstream: https://lore.kernel.org/r/20260923-hawi-gpu-v1-1-0c3c79a1a470@oss.qualcomm.com
  notes: Without it the A8xx GMU votes DDR performance mode (ACV) for every GPU bandwidth level and ignores the Adreno 830 perfmode_bw threshold in 0049.
- `patches/0723-drm-msm-a6xx-Fix-RPMH-dependency-votes.patch`
  source: https://git.kernel.org/next/linux-next/c/eab0aff8965ee17cf972a37eb6456032c45b7acd
  upstream: https://lore.kernel.org/r/20260923-hawi-gpu-v1-3-0c3c79a1a470@oss.qualcomm.com
- `patches/0724-drm-msm-a6xx-Fix-secondary-rail-vote-in-ARC-votes.patch`
  source: https://git.kernel.org/next/linux-next/c/128a0edde50780ed9eb93ab5d2e18ca24c1f1c43
  upstream: https://lore.kernel.org/r/20260923-hawi-gpu-v1-2-0c3c79a1a470@oss.qualcomm.com
- `patches/0726-phy-qualcomm-phy-qcom-eusb2-repeater-Fix-SMB-Power-l.patch`
  source: https://lore.kernel.org/r/20260917-smb-repeater-power-leakage-v1-1-6d7311c3c03e@oss.qualcomm.com
  upstream: https://lore.kernel.org/r/20260917-smb-repeater-power-leakage-v1-1-6d7311c3c03e@oss.qualcomm.com
  notes: Posted, not yet merged. Found on Glymur's SMB2370; the Odin 3 uses the PMIH0108 repeater and the SM8550/SM8650 boards the PM8550B one, which the same exit path covers.
- `patches/0727-drm-msm-dsi-fix-AHB-clock-staying-enabled-across-sus.patch`
  source: https://lore.kernel.org/r/20261006-dsi-ahb-clk-suspend-fix-v1-1-67da848e1b0a@oss.qualcomm.com
  upstream: https://lore.kernel.org/r/20261006-dsi-ahb-clk-suspend-fix-v1-1-67da848e1b0a@oss.qualcomm.com
  notes: Posted, not yet merged. Releases disp_cc_mdss_ahb_clk (and its XO vote) in s2idle; replaces the earlier runtime-PM attempt, which caused display problems around suspend.
- `patches/0730-soundwire-qcom-disable-the-interrupt-before-gating-the-clock.patch`
  source: https://patchwork.kernel.org/project/linux-arm-msm/patch/20261009082639.22662-1-okerixx@gmail.com/
  upstream: https://lore.kernel.org/r/20261009082639.22662-1-okerixx@gmail.com
  notes: Posted, not yet merged. 0564 force-suspends the SoundWire controllers on every system sleep, which runs the clock-gating path this fixes once per suspend.
- `patches/0731-Bluetooth-hci_qca-reset-the-in-band-sleep-state-on-power-off.patch`
  source: https://patchwork.kernel.org/project/linux-arm-msm/patch/20261014180201.57109-1-birk.skyum@pm.me/
  upstream: https://lore.kernel.org/r/20261014180201.57109-1-birk.skyum@pm.me
  notes: Posted, not yet merged (v2). The Odin 3's WCN7860 Bluetooth runs on hci_qca. v2 also stops the IBS work and timers before resetting the state; tested on an SM8750 OnePlus Pad 3.
- `patches/0732-arm64-dts-qcom-disable-the-qce-crypto-engine.patch`
  source: armada
  upstream: local
  notes: Linux 7.3 made CRYPTO_DEV_QCE depend on BROKEN. With fw_devlink.strict=1 the never-probing crypto@1dfa000 kept the interconnect providers out of sync_state, so every BCM stayed at its maximum vote, asleep included. It is also what broke the SM8750 display on 7.3: MDSS does not survive a power collapse while the multimedia NoC is still voted on, so every blank and suspend left the DSI command engine stuck. Any other multimedia NoC user (video decoder, camera) active across a display power cycle still triggers that.

- `patches/1021-wifi-ath12k-fix-single-pdev-frequency-ranges.patch`
  source: https://lore.kernel.org/r/20260715065218.41232-1-gsh20040816@gmail.com
  upstream: https://lore.kernel.org/r/20260715065218.41232-1-gsh20040816@gmail.com
  notes: Backports Shenghan Gao's proposed single-pdev range fix to Linux 7.2.6. The upstream discussion identifies this as a local workaround pending a per-radio regulatory-state redesign; it is not a merged upstream architectural fix.
- `patches/1022-wifi-ath12k-split-WCN7860-scans-by-firmware-ranges.patch`
  source: armada
  upstream: local
  notes: Splits WCN7860 scans by firmware range, preserving one overall timeout and completion. Tested on KONKR Pocket FIT Elite.
- `patches/1023-wifi-ath12k-protect-TX-during-associated-range-scans.patch`
  source: armada
  upstream: local
  notes: Uses single-channel associated scans with TX draining and home-channel rest. Tested on KONKR Pocket FIT Elite.
- `patches/0751-ASoC-codecs-lpass-wsa-macro-use-v2.5-Compander1-addr.patch`
  source: https://git.kernel.org/next/linux-next/c/233d36a96009682208cc4ca1139b9e5641a8bf09
  upstream: https://patch.msgid.link/20260908082806.648797-2-srinivas.kandagatla@oss.qualcomm.com
- `patches/0752-drm-msm-dpu-disable-the-slave-encoder-before-the-mas.patch`
  source: https://git.kernel.org/next/linux-next/c/32d04280ddebb6eb964990931b0f1001f63b35e7
  upstream: https://lore.kernel.org/r/20261002130712.50612-1-26rote@gmail.com
- `patches/0753-drm-msm-dpu-round-up-the-compressed-INTF-width.patch`
  source: https://git.kernel.org/next/linux-next/c/6b93e8b453fa27a1b6a1d472f3ff8663e6811fae
  upstream: https://lore.kernel.org/r/20261004102758.84436-1-26rote@gmail.com
- `patches/0754-PCI-pwrctrl-Power-off-child-devices-on-power-on-fail.patch`
  source: https://git.kernel.org/next/linux-next/c/e95b940b2114e03d1763a022bfda75d8a15702d8
  upstream: https://patch.msgid.link/20260909-pwrtctl-power-on-rallback-v1-1-412ef996ba27@oss.qualcomm.com
- `patches/0755-PCI-qcom-Ignore-ENODEV-after-Root-Port-reset.patch`
  source: https://git.kernel.org/next/linux-next/c/78f27ea27d9870806f51b6f44db7ef6df62f7891
  upstream: https://patch.msgid.link/20260916-topic-pcie_portrec_enodev-v1-1-5dc7bde39552@oss.qualcomm.com
- `patches/0756-PCI-qcom-Block-accesses-to-downstream-devices-on-lin.patch`
  source: https://git.kernel.org/next/linux-next/c/967a73293ae5f57af68e815942078e110c1f6d08
  upstream: https://patch.msgid.link/20260819-ecam_blocker-v2-1-e7a8fdc1c5cb@oss.qualcomm.com
- `patches/0757-serial-qcom-geni-Drop-unsafe-rx_buf-realloc-from-set.patch`
  source: https://git.kernel.org/next/linux-next/c/16ccb505ff021ebbd1207c66e5f68521f6d7fa4c
  upstream: https://patch.msgid.link/20260824-drop-unsafe-rx-buf-realloc-from-setup-fifos-v1-1-52d231c840e1@oss.qualcomm.com
- `patches/0758-usb-typec-ucsi-allow-retries-of-ucsi_resume_work.patch`
  source: https://git.kernel.org/next/linux-next/c/a2463e239443d7a132624700153f0cb1fab13b2c
  upstream: https://patch.msgid.link/20260904234124.2336922-1-jthies@google.com
- `patches/0759-media-iris-Fix-power-off-ordering-to-disable-power-d.patch`
  source: https://git.kernel.org/next/linux-next/c/9cfae7726a9a9f526e8905dbddde355be2674e3d
  upstream: unknown
- `patches/0760-media-iris-reject-open-when-the-session-limit-is-rea.patch`
  source: https://git.kernel.org/next/linux-next/c/397ebadcbc219f6c20d11c0378d8cb7695d015c2
  upstream: unknown
- `patches/0761-media-iris-reference-count-video-instances.patch`
  source: https://git.kernel.org/next/linux-next/c/af5f7df6c8b33bed714ec0aea15a0a2f48900c0a
  upstream: unknown
- `patches/0762-media-iris-reset-AHB-bridge-before-enabling-HW-mode.patch`
  source: https://git.kernel.org/next/linux-next/c/cc330f5589965bcf99307ee9c66deb8a0a53e0ee
  upstream: unknown
- `patches/0763-media-iris-avoid-bit-depth-validation-for-capture-fo.patch`
  source: https://git.kernel.org/next/linux-next/c/40e9c3b3e35c6d65a3a0d3b1483716ad48b046bd
  upstream: unknown
- `patches/0764-media-iris-Fix-iova-allocation-from-restrict-region.patch`
  source: https://git.kernel.org/next/linux-next/c/200473c198b201c308dfb916fb3233074d9407fa
  upstream: unknown
- `patches/0765-clk-qcom-alpha-pll-Check-Lucid-Ole-PLL-status-before.patch`
  source: https://git.kernel.org/next/linux-next/c/eb34e2804ce4ea56efb741e23d598469274a2f94
  upstream: https://lore.kernel.org/r/20260713-sm8450-qol-dispcc-v3-3-56fd05822270@proton.me
- `patches/0766-wifi-ath12k-avoid-IDR-mutation-during-vif-mgmt-TX-cl.patch`
  source: https://git.kernel.org/next/linux-next/c/4aa45334eb23d40bf31c43405daea9b73469f2a6
  upstream: https://patch.msgid.link/20261003092104.520135-6-yaojiale02@163.com
- `patches/0767-wifi-ath12k-avoid-IDR-mutation-during-pending-mgmt-T.patch`
  source: https://git.kernel.org/next/linux-next/c/94c7b50351fd30e1dfe1b4051197a1445d8547e1
  upstream: https://patch.msgid.link/20261003092104.520135-5-yaojiale02@163.com
- `patches/0768-wifi-ath12k-validate-MAC-PHY-capability-count-before.patch`
  source: https://git.kernel.org/next/linux-next/c/86f2537877d6029487811bc3e0cd9e086a196000
  upstream: https://patch.msgid.link/20261003101944.596546-1-yaojiale02@163.com
- `patches/0769-wifi-ath12k-clear-dangling-channel-pointers-on-error.patch`
  source: https://git.kernel.org/next/linux-next/c/507478f6f93864978a399173d4f54c8a987c8235
  upstream: https://patch.msgid.link/20260811020523.387433-1-gonglinkai@kylinos.cn
- `patches/0770-wifi-ath12k-Free-allocated-external-IRQs-on-request_.patch`
  source: https://git.kernel.org/next/linux-next/c/9a78703ec4a895bd2e99bf43bd18d76683126c19
  upstream: https://patch.msgid.link/20260819110215.2485514-3-aaradhana.sahu@oss.qualcomm.com
- `patches/0771-firmware-qcom_scm-align-PAS-resource-table-retry.patch`
  source: https://git.kernel.org/next/linux-next/c/57e43df2e426ac5561ee3832d425e1071772e963
  upstream: https://patch.msgid.link/20260921195636.1925869-3-mukesh.ojha@oss.qualcomm.com
  notes: Follow-up to 0719.
- `patches/0772-media-iris-cancel-sys-error-work-on-driver-removal.patch`
  source: https://git.kernel.org/next/linux-next/c/4524809316482b64ff092afb7e7b0525ce137c75
  upstream: unknown
- `patches/0773-media-iris-fail-firmware-boot-on-invalid-uc_region.patch`
  source: https://git.kernel.org/next/linux-next/c/f301102c17f22f4a140bd9a50281473e6b782f0c
  upstream: unknown
- `patches/0774-media-iris-take-core-lock-when-scanning-the-instance.patch`
  source: https://git.kernel.org/next/linux-next/c/428e6f95e685a06a73868aee95dd94dca7b3a027
  upstream: unknown
- `patches/0775-media-iris-guard-against-a-NULL-hfi_sys_ops-in-the-i.patch`
  source: https://git.kernel.org/next/linux-next/c/95f9e9fc9336ca4e8fb4ff0a76ddbde2f60bdb09
  upstream: unknown
- `patches/0776-wifi-ath12k-use-per-device-max-QMI-chunk-size.patch`
  source: https://git.kernel.org/next/linux-next/c/4e286c780d75831a169b0489afd015214838affd
  upstream: https://patch.msgid.link/20260730-ath12k-align-qmi-memory-v1-1-0fef98dda614@oss.qualcomm.com
- `patches/0777-wifi-ath12k-clear-chunk-paddr-and-size-in-ath12k_qmi.patch`
  source: https://git.kernel.org/next/linux-next/c/a1af8645cf2dcdac5c6b3929e1dcb2274ca9f27e
  upstream: https://patch.msgid.link/20260730-ath12k-align-qmi-memory-v1-2-0fef98dda614@oss.qualcomm.com
- `patches/0778-wifi-ath12k-align-QMI-target-memory-to-64-KB.patch`
  source: https://git.kernel.org/next/linux-next/c/f7f05c443361ebaa503e054e882633913273b3fa
  upstream: https://patch.msgid.link/20260730-ath12k-align-qmi-memory-v1-3-0fef98dda614@oss.qualcomm.com
- `patches/0779-drm-msm-a6xx-Factor-out-RPMh-arc-vote-helpers.patch`
  source: https://git.kernel.org/next/linux-next/c/b5269bf0e1adc2f5d313fce9268b9ac594dc26e0
  upstream: https://lore.kernel.org/r/20260923-hawi-gpu-v1-4-0c3c79a1a470@oss.qualcomm.com
  notes: 0779-0781 complete the series 0723 and 0724 come from; 0779 and 0780 are prerequisites for 0781.
- `patches/0780-drm-msm-a6xx-Add-BX-rail-support-to-GMU-dependency-v.patch`
  source: https://git.kernel.org/next/linux-next/c/020b8eaa1db838c6b58fd500a03218cd1ac76176
  upstream: https://lore.kernel.org/r/20260923-hawi-gpu-v1-5-0c3c79a1a470@oss.qualcomm.com
- `patches/0781-drm-msm-a6xx-Clamp-MX-dependency-vote.patch`
  source: https://git.kernel.org/next/linux-next/c/86f80884fb7f4601a49444a3c36df894b218336e
  upstream: https://lore.kernel.org/r/20260923-hawi-gpu-v1-6-0c3c79a1a470@oss.qualcomm.com
- `patches/0782-drm-msm-a6xx-fix-use-after-free-of-OPP-in-a6xx_pm_re.patch`
  source: https://git.kernel.org/next/linux-next/c/8128ae7af6b4dc95e486c5c0a80839a069df578e
  upstream: https://lore.kernel.org/r/20260929142103.81854-1-roman.demidov.nn@gmail.com
  notes: On the GPU resume path, which runs on every wake.
- `patches/0783-drm-msm-a6xx-check-pm_runtime_resume_and_get-during-.patch`
  source: https://git.kernel.org/next/linux-next/c/e2f57c576f14f96449cfee840860cb9707501d23
  upstream: https://lore.kernel.org/r/20260929142103.81854-2-roman.demidov.nn@gmail.com
- `patches/0784-power-supply-qcom_battmgr-report-the-USB-type-from-U.patch`
  source: https://git.kernel.org/next/linux-next/c/a49f86cd1333c6e12fd37bc0b3234ace10072553
  upstream: https://patch.msgid.link/20261012130053.442-1-26rote@gmail.com
- `patches/0785-power-supply-qcom_battmgr-Notify-charger-supplies-of.patch`
  source: https://git.kernel.org/next/linux-next/c/87fd20da8ca8bacdaa9bff5860167f208077dc51
  upstream: https://patch.msgid.link/20261013-upstream-battmgr-charger-online-v1-1-731973e133a0@gmail.com
- `patches/0786-power-supply-qcom_battmgr-report-full-batteries.patch`
  source: https://git.kernel.org/next/linux-next/c/6c8098e04ee4d233399e40e7311715844910f8f8
  upstream: https://patch.msgid.link/20261008-battmgr-full-v1-1-4f5485a9c421@oss.qualcomm.com
- `patches/0787-serial-qcom-geni-power-the-console-back-up-on-system.patch`
  source: https://git.kernel.org/next/linux-next/c/e95442c31ae65b57ddffdfa609531c549055f308
  upstream: https://patch.msgid.link/20260918-qcom-geni-pm-v1-1-cb587e215607@ixit.cz
- `patches/0788-soc-qcom-geni-se-Fix-endian-conversion-for-serial_pr.patch`
  source: https://git.kernel.org/next/linux-next/c/34da43344c042bf276abace745d7cf6af27699df
  upstream: https://lore.kernel.org/r/20260821-fix-write-to-read-only-firmware-buffer-v3-1-43e6a3abd651@oss.qualcomm.com
  notes: 0788-0791 are the SE firmware-parsing fixes 0792 is based on.
- `patches/0789-soc-qcom-geni-se-Widen-fw_size-to-u32-to-prevent-wra.patch`
  source: https://git.kernel.org/next/linux-next/c/570b3d23794bff9ba8dd99dbd5293dc158a7dbce
  upstream: https://lore.kernel.org/r/20260821-fix-write-to-read-only-firmware-buffer-v3-2-43e6a3abd651@oss.qualcomm.com
- `patches/0790-soc-qcom-geni-se-Fix-fw_end-computed-before-round-up.patch`
  source: https://git.kernel.org/next/linux-next/c/091269da39eb0a52cca2549e9ba522ab7b841ff2
  upstream: https://lore.kernel.org/r/20260821-fix-write-to-read-only-firmware-buffer-v3-3-43e6a3abd651@oss.qualcomm.com
- `patches/0791-soc-qcom-geni-se-Fix-write-to-read-only-firmware-buf.patch`
  source: https://git.kernel.org/next/linux-next/c/f38399670d0701ede4f8da397807aa64d7dc98be
  upstream: https://lore.kernel.org/r/20260821-fix-write-to-read-only-firmware-buffer-v3-4-43e6a3abd651@oss.qualcomm.com
- `patches/0792-soc-qcom-geni-se-provide-PROG_RAM_DEPTH-for-I2C-HUB-.patch`
  source: https://git.kernel.org/next/linux-next/c/803f9950a6c6e0b37ed7f24925feed823703467e
  upstream: https://patch.msgid.link/20260923-topic-sm8x50-i2c-hub-fw-ram-v3-1-44287b4e814b@linaro.org
  notes: The Odin 3's HTR3212 LED controllers sit on I2C hub serial engines.
- `patches/0793-usb-dwc3-qcom-Defer-VBUS-override-update-during-syst.patch`
  source: https://patchwork.kernel.org/project/linux-arm-msm/patch/20261018143126.3978-1-tvlad744@gmail.com/
  upstream: https://lore.kernel.org/r/20261018143126.3978-1-tvlad744@gmail.com
  notes: Posted, not yet merged. On SM8750, unplugging USB during s2idle made dwc3-qcom write QSCRATCH with its clocks off and reset the SoC.
- `patches/0794-soc-qcom-pmic_glink-Hold-back-notifications-over-sys.patch`
  source: https://patchwork.kernel.org/project/linux-arm-msm/patch/20261022164151.592-2-tvlad744@gmail.com/
  upstream: https://lore.kernel.org/r/20261022164151.592-2-tvlad744@gmail.com
  notes: RFC, posted, not yet merged; 0794-0797 are one series. Notifications that arrive from ->prepare() on are passed to the clients from freezable work after resume, so the UCSI connector work can no longer touch suspended devices (the other half of the SM8750 unplug reset). 0713's freezable-workqueue stop-gap stays in place.
- `patches/0795-soc-qcom-pmic_glink-Report-wakeup-events-on-behalf-o.patch`
  source: https://patchwork.kernel.org/project/linux-arm-msm/patch/20261022164151.592-3-tvlad744@gmail.com/
  upstream: https://lore.kernel.org/r/20261022164151.592-3-tvlad744@gmail.com
  notes: RFC, posted, not yet merged.
- `patches/0796-usb-typec-ucsi-glink-Wake-up-the-system-on-connector.patch`
  source: https://patchwork.kernel.org/project/linux-arm-msm/patch/20261022164151.592-4-tvlad744@gmail.com/
  upstream: https://lore.kernel.org/r/20261022164151.592-4-tvlad744@gmail.com
  notes: RFC, posted, not yet merged. A USB-C plug or unplug now wakes the system from s2idle.
- `patches/0797-power-supply-qcom_battmgr-Allow-charger-changes-to-w.patch`
  source: https://patchwork.kernel.org/project/linux-arm-msm/patch/20261022173225.58-1-tvlad744@gmail.com/
  upstream: https://lore.kernel.org/r/20261022173225.58-1-tvlad744@gmail.com
  notes: RFC, posted, not yet merged.
- `patches/0798-power-supply-qcom_battmgr-do-not-report-power_now-on.patch`
  source: https://patchwork.kernel.org/project/linux-arm-msm/patch/20261013002124.332111-1-xiaqinghuan@mail.ustc.edu.cn/
  upstream: https://lore.kernel.org/r/20261013002124.332111-1-xiaqinghuan@mail.ustc.edu.cn
  notes: Posted, not yet merged. The SM8750 firmware fills POWER_NOW from its maximum-load path. Rebased onto 0903, keeping the charge-current properties ahead of POWER_NOW so the SM8750 descriptor still drops only POWER_NOW. SM8750 boards previously matched the SM8550 entry; the new SM8750 variant is otherwise handled like SM8550, since the driver's other variant checks only single out SC8280XP and X1E80100.
- `patches/0799-serial-qcom-geni-Clear-pending-IRQs-while-suspended.patch`
  source: https://patchwork.kernel.org/project/linux-arm-msm/patch/20261021-ack-interrupts-on-suspended-port-v1-1-2747a58ca7cb@oss.qualcomm.com/
  upstream: https://lore.kernel.org/r/20261021-ack-interrupts-on-suspended-port-v1-1-2747a58ca7cb@oss.qualcomm.com
  notes: Posted, not yet merged.
- `patches/0800-dt-bindings-clock-qcom-sm8450-videocc-Fix-clock-inpu.patch`
  source: https://patchwork.kernel.org/project/linux-arm-msm/patch/20261017045817.1506961-2-shengchao.guo@oss.qualcomm.com/
  upstream: https://lore.kernel.org/r/20261017045817.1506961-2-shengchao.guo@oss.qualcomm.com
  notes: Posted, not yet merged (v3). Binding for 0801; the series' Glymur and Nord DTS patches are not carried.
- `patches/0801-arm64-dts-qcom-sm8750-Fix-videocc-clock-inputs.patch`
  source: https://patchwork.kernel.org/project/linux-arm-msm/patch/20261017045817.1506961-4-shengchao.guo@oss.qualcomm.com/
  upstream: https://lore.kernel.org/r/20261017045817.1506961-4-shengchao.guo@oss.qualcomm.com
  notes: Posted, not yet merged (v3). Describes the controller's real inputs (XO, active-only XO, sleep clock); no functional change.
- `patches/0802-wifi-ath12k-Fix-missing-station-power-save-configura.patch`
  source: https://github.com/qualcomm-linux/kernel/commit/9ce0019b303715c1b8b5e37fcca18660da7f1325
  upstream: https://lore.kernel.org/r/20250908015025.1301398-1-miaoqing.pan@oss.qualcomm.com
  notes: Posted, not yet merged; carried in qcom-next. ath12k disables power save when it creates a station vdev and only re-enables it on BSS_CHANGED_PS, which it handled in the link callback while mac80211 reports it through vif_cfg_changed. Without this, the WCN7860 on the Odin 3 stays out of power save for the whole connection.
- `patches/0803-PCI-pwrctrl-Only-destroy-devices-created-by-pwrctrl-.patch`
  source: https://git.kernel.org/torvalds/c/7bf2ebcb7ca1e8814d3d0e35214a8e4b2193a619
  upstream: https://git.kernel.org/torvalds/c/7bf2ebcb7ca1e8814d3d0e35214a8e4b2193a619
- `patches/0804-PCI-pwrctrl-generic-Fix-leaking-array-from-of_regula.patch`
  source: https://git.kernel.org/torvalds/c/ee450e3a2d334c7e6383d8a55ad2d53b3822bacc
  upstream: https://git.kernel.org/torvalds/c/ee450e3a2d334c7e6383d8a55ad2d53b3822bacc
- `patches/0805-PCI-qcom-Only-check-bridge-nodes-for-PERST-GPIOs.patch`
  source: https://git.kernel.org/torvalds/c/1b3b0bc2b3672e928e06997444528f8797579eb2
  upstream: https://git.kernel.org/torvalds/c/1b3b0bc2b3672e928e06997444528f8797579eb2
- `patches/0806-firmware-qcom-tzmem-Use-DO_ONCE_SLEEPABLE-in-qcom_tz.patch`
  source: https://git.kernel.org/torvalds/c/60d4a6edea9ec617725db6dd1e66d96a13bc8d0a
  upstream: https://git.kernel.org/torvalds/c/60d4a6edea9ec617725db6dd1e66d96a13bc8d0a
- `patches/0807-ASoC-qcom-q6apm-dai-wrap-the-position-of-a-full-ring.patch`
  source: https://git.kernel.org/next/linux-next/c/0ea3e0b196f9dcc17b40ac881a6efef06459975b
  upstream: https://patch.msgid.link/20261014162703.10172-2-tvlad744@gmail.com
- `patches/0808-ASoC-qcom-q6apm-reset-the-hw-pointer-with-the-fragme.patch`
  source: https://git.kernel.org/next/linux-next/c/0337b8129cf676b8eb767b2a1f312955760a5460
  upstream: https://patch.msgid.link/20261014162703.10172-3-tvlad744@gmail.com
- `patches/0809-ASoC-qcom-q6asm-dai-wrap-the-position-of-a-full-ring.patch`
  source: https://git.kernel.org/next/linux-next/c/222d04cf55bc5b4b63602454014619c78deda89a
  upstream: https://patch.msgid.link/20261014162703.10172-4-tvlad744@gmail.com
- `patches/0810-ASoC-qcom-q6apm-Guard-callbacks-until-probe-data-is-.patch`
  source: https://github.com/qualcomm-linux/kernel/commit/77fb4931c771292302a16655f5f93d33ae5ef5e8
  upstream: https://lore.kernel.org/r/20261022144130.2443667-2-mohit.sharma@oss.qualcomm.com
  notes: Posted, not yet merged; carried in qcom-next.
- `patches/0811-soc-qcom-apr-Publish-GPR-callback-before-client-prob.patch`
  source: https://github.com/qualcomm-linux/kernel/commit/4e0101dea22b76f128a939ea4f17c89565c5ebda
  upstream: https://lore.kernel.org/r/20261022144130.2443667-3-mohit.sharma@oss.qualcomm.com
  notes: Posted, not yet merged; carried in qcom-next.
- `patches/0812-ASoC-codecs-wcd939x-read-the-SoundWire-port-switches.patch`
  source: https://git.kernel.org/next/linux-next/c/e7860dc5d8d45f6a0e98bfe542c7b776c5ede2a4
  upstream: https://patch.msgid.link/20261007123954.1709-1-26rote@gmail.com
  notes: Rebased onto 0073, which remaps the HPH switches onto the HIFI_PCM port in HPH PCM mode: the channel mask is taken from the remapped channel.
- `patches/0813-usb-typec-ucsi-Skip-CAM-query-when-partner-has-no-al.patch`
  source: https://git.kernel.org/next/linux-next/c/7c590f0716ed3c9ae9809dbc6d488d76c19fdf52
  upstream: https://patch.msgid.link/20260930234611.468765-2-cnfourt@gmail.com
- `patches/0814-drm-msm-dp-wake-threaded-handler-for-HPD-IRQs.patch`
  source: https://github.com/qualcomm-linux/kernel/commit/b09ba7ef33e7d0726065118997ce7d4db62b999e
  upstream: https://lore.kernel.org/r/20260929-msm-dp-mst-v7-33-4b81473185e7@oss.qualcomm.com
  notes: Posted as patch 33 of the DP MST series, not yet merged; carried in qcom-next. Stands alone.
- `patches/0815-phy-qcom-qmp-combo-delay-Type-C-mux-switch-while-DP-.patch`
  source: https://github.com/qualcomm-linux/kernel/commit/47ac5dcc84f730a0c6fc314956d2709748030ccf
  upstream: https://lore.kernel.org/r/20260824-qcom-dp-typec-reconnect-fixes-v1-1-2825e5bf8a96@oss.qualcomm.com
  notes: Posted, not yet merged; carried in qcom-next.
- `patches/0816-arm64-dts-qcom-sm8750-bind-traceNoC-on-the-platform-.patch`
  source: https://github.com/qualcomm-linux/kernel/commit/6f7cb71984a572869d71be4baff76cdbfe8a07b2
  upstream: https://lore.kernel.org/r/20260710-fix-tracenoc-probe-issue-v6-4-41eb36fef8d9@oss.qualcomm.com
  notes: Posted, not yet merged; carried in qcom-next.
- `patches/0817-arm64-dts-qcom-sm8250-Fix-PCIe-wake-GPIO-polarity.patch`
  source: https://github.com/qualcomm-linux/kernel/commit/a44a69c59a22628efcfbc34b61f27881e0235945
  upstream: https://lore.kernel.org/r/20260611-wake-v2-6-2744251b1181@oss.qualcomm.com
  notes: Posted, not yet merged; carried in qcom-next.
- `patches/0818-wifi-ath12k-fix-incorrect-channel-survey-index.patch`
  source: https://github.com/qualcomm-linux/kernel/commit/193c7df72d5b3c784c5f664c75a38eedd020b331
  upstream: https://lore.kernel.org/r/20260210024440.3422264-1-yingying.tang@oss.qualcomm.com
  notes: Posted, not yet merged; carried in qcom-next.
- `patches/0819-wifi-ath11k-fix-sporadic-WLAN-initialization-failure.patch`
  source: https://git.kernel.org/torvalds/c/32ec8488d75d122768b1977501bcb5ec799230c4
  upstream: https://git.kernel.org/torvalds/c/32ec8488d75d122768b1977501bcb5ec799230c4
- `patches/0820-wifi-ath11k-unregister-PM-notifier-on-QMI-init-failu.patch`
  source: https://git.kernel.org/torvalds/c/1d8e73163ef933624341075f576e2f36ef9133f7
  upstream: https://git.kernel.org/torvalds/c/1d8e73163ef933624341075f576e2f36ef9133f7
