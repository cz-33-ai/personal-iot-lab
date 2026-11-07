"""Dependency-free verification of the OFFLINE mock PWI demo."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "examples"))
from prepare_for_sleep_simulator import get_mock_devices, build_plan, run  # noqa: E402


class PwiDemoTests(unittest.TestCase):
    def test_default_dry_run_does_not_claim_execution(self):
        result = run()
        self.assertEqual(result["mode"], "dry_run")
        self.assertFalse(result["physical_devices_controlled"])
        self.assertEqual(result["result"], "plan_ready")
        self.assertTrue(all(a["status"] == "planned" for a in result["actions"]))

    def test_mock_apply_confirms_four_actions(self):
        result = run(apply=True)
        self.assertEqual(result["result"], "simulated_complete")
        self.assertEqual([a["status"] for a in result["actions"]], ["confirmed"] * 4)
        self.assertTrue(all(a["verification"] == "simulated_state_readback" for a in result["actions"]))

    def test_offline_device_is_not_marked_confirmed(self):
        result = run(scenario="offline", apply=True)
        self.assertEqual(result["result"], "partial")
        curtain = next(a for a in result["actions"] if a["entity_id"] == "bedroom.curtains")
        self.assertEqual(curtain["status"], "unavailable")

    def test_no_unnecessary_commands(self):
        result = run(scenario="partially-ready", apply=True)
        self.assertEqual(result["actions"][0]["status"], "already_satisfied")
        self.assertEqual(result["actions"][3]["status"], "already_satisfied")

    def test_preference_is_applied_to_target(self):
        result = run(target_temperature=23)
        ac = next(a for a in result["actions"] if a["entity_id"] == "bedroom.ac")
        self.assertEqual(ac["target"], 23)

    def test_unavailable_capability_is_explicit(self):
        d = get_mock_devices("default")
        del d["bedroom.speaker"]
        plan = build_plan(d)
        self.assertEqual(plan[-1]["status"], "unsupported")


if __name__ == "__main__":
    unittest.main()
