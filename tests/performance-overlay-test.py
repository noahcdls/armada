#!/usr/bin/env python3
import importlib.machinery
import importlib.util
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "system_files/usr/lib/armada"))
loader = importlib.machinery.SourceFileLoader(
    "overlay_control", str(ROOT / "system_files/usr/libexec/armada/armada-control"),
)
spec = importlib.util.spec_from_loader(loader.name, loader)
control = importlib.util.module_from_spec(spec)
loader.exec_module(control)


class PerformanceOverlayTest(unittest.TestCase):
    def setUp(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.config = Path(directory.name) / "performance-overlay.conf"
        mock = patch.object(control, "PERFORMANCE_OVERLAY_CONFIG", self.config)
        mock.start()
        self.addCleanup(mock.stop)

    def test_default_off_and_persistence(self):
        self.assertEqual(control.action_get_overlay_steam_ui_enabled({}), {"enabled": False})
        for enabled in (True, False):
            self.assertEqual(control.action_set_overlay_steam_ui_enabled({"enabled": enabled}), {"enabled": enabled})
            # mangoapp (mangohud 0009) parses exactly this line
            self.assertEqual(self.config.read_text(), f"steam_ui={int(enabled)}\n")
            self.assertEqual(control.action_get_overlay_steam_ui_enabled({}), {"enabled": enabled})

    def test_rejects_non_bool(self):
        with self.assertRaises(ValueError):
            control.action_set_overlay_steam_ui_enabled({"enabled": "1"})
        self.assertFalse(self.config.exists())

    def test_registered_actions(self):
        self.assertIn("get_overlay_steam_ui_enabled", control.ACTIONS)
        self.assertIn("set_overlay_steam_ui_enabled", control.ACTIONS)


if __name__ == "__main__":
    unittest.main()
