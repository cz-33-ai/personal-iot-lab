"""PWI zero-hardware educational demo. Uses mock devices ONLY.

No network access, real IoT control, LLM calls, or persistent memory.
"""

from __future__ import annotations

import argparse
import json
from copy import deepcopy


MOCK_DEVICES = {
    "bedroom.main_light": {"capability": "light.turn_off", "state": "on", "available": True},
    "bedroom.curtains": {"capability": "cover.close", "state": "open", "available": True},
    "bedroom.ac": {"capability": "climate.set_temperature", "state": 25, "available": True},
    "bedroom.speaker": {"capability": "media.stop", "state": "playing", "available": True},
}


def get_mock_devices(scenario: str) -> dict:
    """Return example inventory; none of these are real user devices."""
    devices = deepcopy(MOCK_DEVICES)
    if scenario == "offline":
        devices["bedroom.curtains"]["available"] = False
    elif scenario == "partially-ready":
        devices["bedroom.main_light"]["state"] = "off"
        devices["bedroom.speaker"]["state"] = "stopped"
    return devices


def build_plan(devices: dict, target_temperature: int = 22) -> list[dict]:
    """Deterministic mapping of a single example intent to desired device state.

    This is a teaching stand-in for an actual Personal Agent's planner.
    """
    desired = [
        ("bedroom.main_light", "light.turn_off", "off"),
        ("bedroom.curtains", "cover.close", "closed"),
        ("bedroom.ac", "climate.set_temperature", target_temperature),
        ("bedroom.speaker", "media.stop", "stopped"),
    ]
    plan = []
    for entity_id, capability, target in desired:
        device = devices.get(entity_id)
        if device is None:
            plan.append({"entity_id": entity_id, "capability": capability, "target": target,
                         "status": "unsupported", "reason": "Entity not discovered"})
        elif device["capability"] != capability:
            plan.append({"entity_id": entity_id, "capability": capability, "target": target,
                         "status": "unsupported", "reason": "Capability not available"})
        elif not device["available"]:
            plan.append({"entity_id": entity_id, "capability": capability, "target": target,
                         "status": "unavailable", "reason": "Mock device is offline"})
        elif device["state"] == target:
            plan.append({"entity_id": entity_id, "capability": capability, "target": target,
                         "status": "already_satisfied", "observed_state": device["state"]})
        else:
            plan.append({"entity_id": entity_id, "capability": capability, "target": target,
                         "status": "planned", "observed_state": device["state"]})
    return plan


def simulate_execution(devices: dict, plan: list[dict]) -> list[dict]:
    """Mock application and mock state read-back. NEVER touches real hardware."""
    results = []
    for action in plan:
        result = dict(action)
        if result["status"] == "planned":
            entity_id = result["entity_id"]
            devices[entity_id]["state"] = result["target"]
            readback = devices[entity_id]["state"]
            result["observed_state"] = readback
            result["status"] = "confirmed" if readback == result["target"] else "unverified"
            result["verification"] = "simulated_state_readback"
        results.append(result)
    return results


def run(scenario: str = "default", apply: bool = False, target_temperature: int = 22) -> dict:
    devices = get_mock_devices(scenario)
    actions = build_plan(devices, target_temperature)
    if apply:
        actions = simulate_execution(devices, actions)
    return {
        "demo": "PWI / Prepare for Sleep",
        "simulation": True,
        "external_agent_connected": False,
        "physical_devices_controlled": False,
        "mode": "simulated_apply" if apply else "dry_run",
        "scenario": scenario,
        "user_intent_example": "I'm getting ready for bed",
        "preference_example": {"sleep_temperature_c": target_temperature},
        "actions": actions,
        "result": "partial" if any(a["status"] in ("unavailable", "unsupported", "unverified") for a in actions)
                  else "simulated_complete" if apply else "plan_ready",
        "note": "Educational mock only. No real Agent, MQTT, Home Assistant, or hardware was used.",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Offline mock PWI Prepare for Sleep demo")
    parser.add_argument("--scenario", choices=["default", "offline", "partially-ready"], default="default")
    parser.add_argument("--apply", action="store_true", help="Apply to MOCK inventory only (never real devices)")
    parser.add_argument("--temperature", type=int, default=22, help="Example preferred target temperature °C")
    args = parser.parse_args()
    if not 16 <= args.temperature <= 30:
        parser.error("--temperature must be between 16 and 30 °C")
    print(json.dumps(run(args.scenario, args.apply, args.temperature), indent=2))


if __name__ == "__main__":
    main()
