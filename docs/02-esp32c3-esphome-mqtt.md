# Experiment 02 — ESP32-C3, ESPHome and MQTT

## Goal
Connect an ESP32-C3 to Wi-Fi and a local Mosquitto broker, then verify messages in both directions without attaching a sensor or LED.

Tested software: ESPHome 2026.10.2; ESP-IDF 5.5.6. Your board and software versions may differ.

## 1. Validate the configuration

Keep credentials in a local, untracked secrets file. Never publish Wi-Fi or MQTT passwords.

```bash
esphome version
esphome config esp32c3-mqtt.yaml
```

A successful validation ends with:

```text
INFO Configuration is valid!
```

## 2. Identify the serial device

```bash
ls /dev/cu.*
```

On macOS, USB serial devices commonly appear as `/dev/cu.*`. Identify the ESP32 port from the connected hardware; its name can change after reconnecting.

If flashing reports that the port is busy, close browser-based flashing tools and check:

```bash
lsof -nP /dev/cu.<YOUR_ESP32_SERIAL_DEVICE>
```

## 3. MQTT topics

| Topic | Direction | Purpose |
|---|---|---|
| `esp32c3/heartbeat` | ESP32 → broker | Periodic heartbeat |
| `esp32c3/command` | Mac → ESP32 | Incoming test command |
| `esp32c3/status` | ESP32 → broker | Online/offline state |

The example publishes a heartbeat every five seconds and logs the payload received on the command topic.

## 4. Subscribe to ESP32 messages

Replace `<BROKER_IP>` with the current LAN address of the broker:

```bash
mosquitto_sub -h <BROKER_IP> -p 1883 -t 'esp32c3/#' -v
```

Example messages:

```text
esp32c3/status online
esp32c3/heartbeat Hello from ESP32-C3
```

## 5. Send a command to the ESP32

In another Terminal window:

```bash
mosquitto_pub -h <BROKER_IP> -p 1883 -t 'esp32c3/command' -m 'Hello from Mac'
```

The ESPHome log should show the received command.

**Result:** The ESP32-C3 joined Wi-Fi, connected to Mosquitto, published a heartbeat, and received a command. This verifies the network path before adding GPIO hardware.

## Troubleshooting

- Broker connection fails: confirm Mosquitto listens on a LAN interface, not only loopback.
- Serial port busy: close other programs using the USB serial device.
- Wi-Fi warning appears: inspect subsequent logs; a transient warning may be followed by a successful reconnect.
- No heartbeat: check ESPHome Wi-Fi/MQTT logs, broker address, and topic prefix.
