# Experiment 03 — Zigbee sensors through Zigbee2MQTT

## Goal
Read Zigbee sensor state through MQTT without writing a custom Zigbee application.

## Data path

```text
Zigbee sensor
   |
Zigbee coordinator
   |
Zigbee2MQTT
   |
Mosquitto MQTT broker
   |
mosquitto_sub / another MQTT client
```

## 1. Check the bridge

```bash
mosquitto_sub -h <BROKER_IP> -p 1883 -t 'zigbee2mqtt/bridge/state' -v
```

A connected bridge publishes a state similar to:

```text
zigbee2mqtt/bridge/state {"state":"online"}
```

## 2. Inspect all Zigbee2MQTT messages

```bash
mosquitto_sub -h <BROKER_IP> -p 1883 -t 'zigbee2mqtt/#' -v
```

The `#` wildcard matches all topic levels below the base topic.

To listen to two individual device topics:

```bash
mosquitto_sub -h <BROKER_IP> -p 1883 \
  -t 'zigbee2mqtt/motion_sensor' \
  -t 'zigbee2mqtt/temperature_sensor' -v
```

Quote topic names containing shell-special characters. For example, an ampersand (`&`) must be quoted so the shell treats it as part of the topic.

## 3. Motion and illuminance sensor

Observed JSON state included fields such as:

- `occupancy`: whether motion is detected.
- `illuminance`: measured light level.
- `battery`: reported battery percentage.
- `linkquality`: Zigbee link-quality indicator.
- `sensitivity` and `keep_time`: device-specific settings.

The occupancy state changed between `false` and `true`, and illuminance values changed with the environment.

**Result:** MQTT messages from the motion/illuminance sensor were observed successfully.

## 4. Temperature and humidity sensor

A display-equipped sensor (model reported by Zigbee2MQTT as TS0201) showed changing temperature and humidity values in the UI. During one observation window, however, a Terminal subscriber did not print a corresponding message. A later device activity entry showed temperature and humidity state changes.

This is an unresolved reporting/timing question, not proof of a defective sensor.

### Controlled follow-up

1. Start a broad subscriber before touching the sensor:

   ```bash
   mosquitto_sub -h <BROKER_IP> -p 1883 -t 'zigbee2mqtt/#' -v
   ```

2. Note the time and displayed values.
3. Warm or cool the sensor gradually.
4. Wait for a report.
5. Compare the terminal output with the Zigbee2MQTT activity timestamp.
6. If no message appears, check the exact friendly name/topic.

## Lessons

- Zigbee2MQTT exposes Zigbee device state through MQTT.
- Topic spelling matters.
- A dashboard state and a live Terminal subscription are different observations; compare them over the same time window.
- Do not infer a hardware fault from one missing report.

Device IEEE addresses, MAC addresses, private IP assignments, household-specific names, and raw bridge configuration dumps are intentionally excluded from this public tutorial.
