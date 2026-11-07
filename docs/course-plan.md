# Building the Physical World Interface — Curriculum Draft

**Goal:** Teach learners to construct a physical-world interface that can **perceive**, **understand device state/capabilities**, **act safely**, and report feedback to an AI Agent and its broader Context Layer.

This is an evolving educational track. **Module 00 is a runnable offline teaching lesson**; the other modules are a curriculum plan or historical experiments, not yet fully validated standalone courses. Lessons should be marked complete only when their hands-on acceptance tests have been verified.

| Module | Topic | Practical outcome |
|---|---|---|
| [00](../course/module-00-intent-to-physical-outcome.md) | Big Picture: Personal Agent ↔ Physical World | Run offline demo; explain intent, device capabilities, feedback and boundaries |
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


## Start learning now

**[Module 00 — From User Intent to Physical Outcomes](../course/module-00-intent-to-physical-outcome.md)** is the first executable lesson. It uses the no-hardware simulator, exercises and assessments. It must not be described as real Agent or physical-world control.

The next teaching milestone is [#11 — Validate the first PWI teaching module](https://github.com/cz-33-ai/physical-world-interface/issues/11).
