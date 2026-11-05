# Experiment 01 — Local MQTT broker and LAN connectivity

## Goal
Understand MQTT publish/subscribe and make a Mosquitto broker reachable by devices on the same local network.

## 1. Check the listener

```bash
lsof -nP -iTCP:1883 -sTCP:LISTEN
```

This lists processes listening on TCP port 1883. If the output shows `127.0.0.1:1883` or `[::1]:1883`, the broker is listening only on loopback. Other devices on the LAN cannot reach it through the Mac's LAN address.

After configuring Mosquitto to listen on the appropriate LAN interface, run the same command again. In our test, the listener changed to `*:1883`.

Do not expose an unauthenticated MQTT broker to the public Internet.

## 2. Test locally

Open two Terminal windows.

**Terminal A — subscribe:**

```bash
mosquitto_sub -h 127.0.0.1 -p 1883 -t 'lab/test' -v
```

**Terminal B — publish:**

```bash
mosquitto_pub -h 127.0.0.1 -p 1883 -t 'lab/test' -m 'Hello_MQTT' -d
```

Expected subscriber output:

```text
lab/test Hello_MQTT
```

## 3. Test through the LAN

Replace `<BROKER_IP>` with the current LAN address of the machine running Mosquitto:

```bash
mosquitto_pub -h <BROKER_IP> -p 1883 -t 'lab/test' -m 'Hello LAN!'
```

Keep a subscriber listening on the same topic to verify the payload arrives.

## Command reference

| Option | Meaning |
|---|---|
| `-h` | Broker host or IP |
| `-p` | Broker port |
| `-t` | MQTT topic |
| `-m` | Message payload |
| `-v` | Print topic and payload |
| `-d` | Show MQTT debug information |

## Lessons

- A running broker may still be unreachable from another device.
- Loopback is not the same as a LAN interface.
- Start the subscriber before publishing non-retained test messages.
- Use broker logs and `lsof` together to diagnose connectivity.

**Result:** Local publish/subscribe passed; after changing the listener configuration, the broker accepted a LAN-side connection.
