# Physical World Interface (PWI)

> [!IMPORTANT]
> ### 🎯 WHERE TO START: **[PWI MISSION CONTROL — Open your To-Do Dashboard](START_HERE.md)**
> **Current stage:** M1 · Unified Device Hub  
> **One task to do NOW:** **[#6 — Install Home Assistant & open the dashboard](https://github.com/cz-33-ai/physical-world-interface/issues/6)**  
> [View all open issues](https://github.com/cz-33-ai/physical-world-interface/issues?q=is%3Aissue+is%3Aopen) · [View tasks assigned to me](https://github.com/cz-33-ai/physical-world-interface/issues?q=is%3Aissue+is%3Aopen+assignee%3A%40me)

| ✅ DONE | 🔵 NOW | ⏭️ NEXT | 🔭 LATER |
|:---:|:---:|:---:|:---:|
| MQTT + Zigbee + ESP32 basic connectivity | [Install Home Assistant · #6](https://github.com/cz-33-ai/physical-world-interface/issues/6) | [Connect Zigbee2MQTT · #7](https://github.com/cz-33-ai/physical-world-interface/issues/7) | [Agent “Prepare for Sleep” · #4](https://github.com/cz-33-ai/physical-world-interface/issues/4) |

**Can't remember what to do? Bookmark [START_HERE.md](START_HERE.md).** It is the curated home for the current task, next steps and full project milestones.

---


**Perceive, understand, and act in the physical world — a unified physical capability layer for Personal Agents.**

PWI is a subsystem of the larger **Personal Agent Platform**. Its mission is not merely to control smart-home devices: it aims to help an Agent **observe the physical environment, understand device state and capabilities, execute authorized multi-device actions, and receive verifiable feedback**.

The home IoT setup is our first experimental environment, **not the project's scope limit**. The architecture should eventually accommodate offices, wearables, vehicles, and custom embedded devices.

## The idea

Imagine a user tells the Personal Agent: **“I'm getting ready for bed.”**

The Agent retrieves relevant preferences from its Personal Context Layer, checks the environment's available capabilities and current states through PWI, and forms a plan: turn off the light, close the curtains, adjust the air conditioner, and stop music if it is playing. PWI translates these **semantic operations** into actual device commands and reports verified results or uncertainty.

The Agent **owns intent and planning**. The overarching Personal Context Layer **owns personal memory and evolving facts**. PWI **owns the physical device interface and execution evidence**. Useful observations and outcomes can be handed to the platform's context ingestion pipeline without creating a second memory system inside PWI.

## Architecture at a glance

```text
          Personal Agent + Personal Context Layer
                        |
                Intent-informed actions
                        |
                        v
                  PWI Interface
       Perception | Capabilities | Actions | Feedback
                        |
                        v
                 Device Hub / Adapters
                  Home Assistant (v1)
                        |
              +---------+----------+
              |         |          |
          Zigbee2MQTT  ESPHome   Other integrations
              |         |          |
           Sensors   ESP32 I/O   Lights / Covers / AC
              |         |          |
              +---------+----------+
                        |
                 State and event output
                        |
                        v
              Platform Context Ingestion
```

See [PWI architecture v0.1](docs/architecture/pwi-overview.md) for responsibilities, boundaries, example flows, and proposed contracts. The approved high-level Personal Agent Platform architecture remains authoritative in its own repository; this diagram only expands the **Physical Devices** capability area.

## Leverage the existing ecosystem

We want to **reuse proven infrastructure** rather than reimplement device protocols.

| Concern | Initial choice | Role |
|---|---|---|
| Device hub and control | Home Assistant *(planned)* | Device model, availability, operations, scenes/scripts |
| Zigbee connectivity | Zigbee2MQTT + coordinator | Zigbee device integration |
| Message transport | Mosquitto / MQTT | Publish-subscribe telemetry and control |
| Custom embedded nodes | ESP32-C3 + ESPHome | Edge sensing and actuation |
| Agent connection | MCP and/or API *(to evaluate)* | Scoped capability discovery, query and actions |
| Physical event output | Typed events *(to design)* | Observations and action feedback for upstream Context ingestion |

**Status:** The MQTT, ESP32-C3 and Zigbee motion-sensor baseline has been tested. Home Assistant integration, Agent orchestration, action feedback contracts, and end-to-end “prepare for sleep” remain future work. We do not claim that devices we have not connected are controlled.

## Project documents

| Read | Purpose |
|---|---|
| [Architecture](docs/architecture/pwi-overview.md) | High-level vision, middle-level modules, boundaries, flows |
| [Roadmap](docs/roadmap.md) | Milestones M0–M5, acceptance criteria and current baseline |
| [GitHub workflow](docs/project-workflow.md) | Issue/PR conventions, source of truth and publication checks |
| [Course plan](docs/course-plan.md) | Learning modules and future capstone |
| [ADRs](docs/adr/README.md) | How major architecture choices will be recorded |

## Existing hands-on experiments

These are public, sanitized versions of experiments. Raw lab evidence is kept in a separate private notebook.

1. [MQTT broker and local network](docs/01-mqtt-broker-and-lan-test.md)
2. [ESP32-C3 + ESPHome + MQTT](docs/02-esp32c3-esphome-mqtt.md)
3. [Zigbee2MQTT sensor observations](docs/03-zigbee2mqtt-sensor-observations.md)
4. [Credential-free ESPHome example](config/esp32c3-mqtt.example.yaml)

## Planned code organization

The current repository is documentation-first. **These directories describe the direction, not implemented software**:

```text
docs/            Architecture, roadmap, ADRs and verified tutorials
config/          Sanitized reproducible configuration examples
integrations/    Home Assistant and future device adapters (planned)
packages/        Device/capability/action/event contracts (planned)
examples/        Minimal integrations and end-to-end demonstrations (planned)
tests/           Contract, hardware-in-the-loop and failure tests (planned)
course/          Reproducible teaching modules (planned)
```

Build incrementally, beginning with Home Assistant and one controllable actuator. Do not add empty scaffolding before its first real implementation.

## Guiding principles

- **Perception + action:** a successful interface reports both sensed state and the observed result of commands.
- **Semantic capabilities:** ask to `set_light_brightness`, not to manipulate a vendor-specific GPIO from the Agent.
- **Separation of concerns:** Agent planning and long-term personal context stay outside PWI.
- **Reuse and replaceability:** adopt mature integrations but avoid unnecessary lock-in.
- **Local-first and least privilege:** physical control should work locally; agent permissions must be explicit.
- **Evidence over assertions:** distinguish requested, dispatched, confirmed, failed and unverified action states.
- **Privacy by default:** never publish real credentials, private addresses, device identifiers, household labels or unreviewed traces.

See the [project workflow](docs/project-workflow.md) before contributing or publishing experiments.
