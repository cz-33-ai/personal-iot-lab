# Quick Start — Try PWI Without Hardware

**Audience:** people who want to understand PWI in five minutes.  
**Status:** reproducible **offline teaching simulation**, not a live Agent or hardware integration.

## Prerequisite

Python **3.10+**. No extra packages, API keys, network access, IoT devices or Home Assistant are required for this particular demo.

## 1. Clone and run

```bash
git clone https://github.com/cz-33-ai/physical-world-interface.git
cd physical-world-interface
python3 examples/prepare_for_sleep_simulator.py
```

This prints a JSON **dry run**: a fixed example user intent, an example sleep-temperature preference and a planned set of device operations. It does **not** execute physical actions.

## 2. Simulate actions and observe feedback

```bash
python3 examples/prepare_for_sleep_simulator.py --apply
```

The `--apply` option **only mutates mock device state inside the Python process**. It does not communicate with any physical device.

Try a partial failure:

```bash
python3 examples/prepare_for_sleep_simulator.py --apply --scenario offline
```

The mock curtains are unavailable. The output marks that action as `unavailable` and reports the overall result as `partial`.

Try an already-prepared room and a different example preference:

```bash
python3 examples/prepare_for_sleep_simulator.py --apply --scenario partially-ready --temperature 23
```

This demonstrates `already_satisfied` and avoids unnecessary mock operations.

## 3. Check the implementation

```bash
python3 -m unittest discover -s tests -v
```

The current test suite covers planning versus applying, simulated state feedback, offline device, no-op behavior, target temperature and unsupported capabilities.

## What this demonstrates

```text
Example intent: "I'm getting ready for bed"
    |
    v
Example preference + mock capability inventory
    |
    v
Desired states: off / closed / temperature / stopped
    |
    v
Per-device action plan
    |
    v
[Optional simulation only] Apply and read back mock state
    |
    v
Structured per-device results and overall outcome
```

## What this does NOT demonstrate

- There is no LLM, Personal Agent or real Personal Context Layer.
- There is no real Home Assistant, Zigbee, ESP32, MQTT or device actuation.
- `confirmed` means **the simulator's mock state read-back** was successful; it is NOT proof of a physical operation.
- This is a deterministic scaffold for understanding *PWI's interface*, not a production control gateway.

**Next:** read the [real-device integration roadmap](docs/roadmap.md) and the [Prepare for Sleep Demo spec](docs/demos/prepare-for-sleep.md).

## Existing hardware learning path

If you want the previously validated IoT fundamentals instead, start with:
- [MQTT broker and LAN](docs/01-mqtt-broker-and-lan-test.md)
- [ESP32-C3 + ESPHome + MQTT](docs/02-esp32c3-esphome-mqtt.md)
- [Zigbee2MQTT sensor observations](docs/03-zigbee2mqtt-sensor-observations.md)

These are sanitized reports of previous tests, not a one-command installation of the full PWI platform.
