# Personal IoT Lab

A hands-on learning journey into connected devices, local-first smart home systems, and practical IoT engineering.

The experiments start with a local MQTT broker, then connect ESP32-C3 firmware built with ESPHome and Zigbee devices exposed through Zigbee2MQTT.

This repository is the **public, sanitized companion** to a private lab notebook. It focuses on reproducible steps, explanations, observed results, and lessons learned. Personal network details, credentials, and device identifiers are intentionally excluded.

## Experiments

| Experiment | What it covers | Status |
|---|---|---|
| 01 — MQTT broker and LAN connectivity | Mosquitto, topics, publish/subscribe, listener binding | Completed |
| 02 — ESP32-C3 with ESPHome and MQTT | Firmware validation/flashing, Wi-Fi, heartbeat and command round-trip | Completed |
| 03 — Zigbee2MQTT sensor observations | Motion/illuminance and temperature/humidity topics | In progress: one reporting-timing question remains |

## Repository structure

```text
personal-iot-lab/
├── config/
│   └── esp32c3-mqtt.example.yaml
└── docs/
    ├── 01-mqtt-broker-and-lan-test.md
    ├── 02-esp32c3-esphome-mqtt.md
    └── 03-zigbee2mqtt-sensor-observations.md
```

## Principles

- Prefer local-first experiments that can be reproduced without cloud dependencies.
- Explain commands and outputs, not just paste them.
- Separate verified observations from hypotheses and open questions.
- Never publish Wi-Fi credentials, MQTT credentials, API keys, private IP assignments, MAC/IEEE addresses, or household-specific information.
- Use placeholders such as `<BROKER_IP>` and ESPHome `!secret` references in examples.

## Companion private notebook

The detailed, private record (including full learning notes and troubleshooting history) is maintained separately and is not mirrored automatically into this public repository.

## Disclaimer

These notes describe a personal test environment. Network addresses, device names, firmware versions, and UI details may differ in other setups. Do not expose an unauthenticated MQTT broker to the public Internet.
