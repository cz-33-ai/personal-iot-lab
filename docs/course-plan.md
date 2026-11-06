# Building the Physical World Interface — Curriculum Draft

**Goal:** Teach learners to construct a physical-world interface that can **perceive**, **understand device state/capabilities**, **act safely**, and report feedback to an AI Agent and its broader Context Layer.

This is an intended educational track. Lessons should be published as complete only after the corresponding lab has been verified.

| Module | Topic | Practical outcome |
|---|---|---|
| 00 | Big Picture: Personal Agent ↔ Physical World | Explain boundaries, perception/action loops and subsystem contracts |
| 01 | Networking, Terminal, USB Serial | Diagnose ports, hosts and device connections |
| 02 | MQTT and Messaging | Publish/subscribe with Mosquitto |
| 03 | Zigbee and Zigbee2MQTT | Read sensor telemetry through a coordinator |
| 04 | ESP32 and ESPHome | Bring an embedded node online |
| 05 | Sensors, Actuators and GPIO | Measure input, perform safe low-voltage actions |
| 06 | Home Assistant device model | Discover entities, areas, capabilities and states |
| 07 | Action orchestration and feedback | Build repeatable scripts with state confirmation |
| 08 | Agent tool interface and authorization | Expose scoped physical capabilities to an Agent |
| 09 | Physical telemetry to Context | Form timestamped, provenance-aware events |
| 10 | Reliability, safety and testing | Handle disconnects, stale state, retries and restarts |
| Capstone | Prepare for Sleep | Intent → contextual plan → device operations → verified results |

## Lesson template

Every module will include:

1. Learning objectives and prerequisites.
2. System architecture position.
3. Hardware/software bill of materials.
4. Step-by-step commands/configuration.
5. Expected and **actually observed** results.
6. Troubleshooting and failure-mode analysis.
7. Exercises with evaluation criteria.
8. Connection to the final Agent-controlled environment.

A student should finish with a system-engineering mindset, not just a collection of device-specific tricks.
