# Physical World Interface (PWI) — Architecture v0.1

> **Status:** Concept proposal. This is a subsystem of Personal Agent Platform, **not** a replacement for its approved v1.0 architecture.

## Mission

Make the physical world **observable, understandable, and actionable** through a uniform set of capabilities that Personal Agents can discover and safely invoke.

PWI is **not only a smart-home controller**. Home is our first reproducible lab; future physical domains can include offices, wearables, vehicles, and custom embedded devices.

## What belongs to PWI

1. **Perception:** ingest telemetry, state changes, device availability, and the outcome of physical actions.
2. **Physical understanding:** resolve device identity, location, capabilities and operating state; distinguish reported observations from inferred physical state.
3. **Action:** expose authorized, semantically meaningful operations such as `set_light_brightness` or `close_cover`.
4. **Execution:** dispatch commands through adapters, monitor acknowledgements and observed state, report partial failure or uncertainty.
5. **Event output:** provide structured observations and action outcomes to the overarching Personal Context Platform for qualification and possible retention.

**Boundary:** The Personal Agent interprets user intent and plans tasks. The Personal Context Layer owns personal preferences, long-term memory, temporal facts, and task-specific context. PWI operates the physical capability layer and reports evidence; it does not become a second personal memory system.

## High-level interface

```text
                     Personal Agent Platform
                User Intent / Task / Context
                             |
                             | semantic capability request
                             v
               +---------------------------+
               |  PWI Capability Gateway   |
               | discover / query / action |
               | authz / policy / results  |
               +---------------------------+
                    |                ^
               command plan     state/feedback
                    v                |
               +---------------------------+
               | Device Integration Layer  |
               | Home Assistant (initial)  |
               +---------------------------+
                    |        |        |
                Zigbee    ESPHome    Native/
                / MQTT      API      Matter/IR
                    |        |        |
                    v        v        v
                  Physical Devices and Sensors
                             |
                        observations
                             v
                 PWI Event / State Output
                             |
                             v
                 Personal Context Layer
              (qualification and evolution)
```

*Arrows illustrate responsibilities and do not prescribe a single network topology or transport.*

## Why leverage Home Assistant?

Home Assistant already provides device integration, entity/state modeling, area organization, services, scenes, scripts, and automations. The initial PWI should reuse these instead of inventing another device hub. Zigbee2MQTT, Mosquitto and ESPHome remain useful underneath it.

**Initial integration choice:** Home Assistant first, with MQTT/Zigbee2MQTT and ESPHome behind it. **Future choices:** MCP and/or API-based gateway with explicit capabilities and authorization. Specific transport and schema decisions are subject to experiments and ADRs.

## Canonical example: “I'm getting ready for bed”

1. Agent interprets the goal: prepare the bedroom for sleep.
2. Agent obtains personal preferences from the **Personal Context Layer**.
3. PWI exposes available physical capabilities and reliable current state.
4. Agent forms desired state and invokes an authorized environment operation.
5. Integration layer operates lights, curtains, climate control and media **only where compatible hardware/integrations are actually available**.
6. PWI reports `requested`, `dispatched`, `confirmed`, `failed` or `unverified` results per action.
7. Relevant observations and outcomes are offered to the platform's context ingestion path.

Do not represent command dispatch as physical success; prefer observed state feedback.

## Key entities and contracts (proposed)

| Concept | Meaning |
|---|---|
| `Device` | Physical device with stable local identity |
| `Capability` | Abstract action/observation feature, e.g. `light.set_brightness` |
| `Entity` | Addressable functional endpoint provided by an integration |
| `ReportedState` | Last observed state, freshness and source |
| `DesiredState` | State requested by a user/agent |
| `ActionRequest` | Authorized semantic operation and parameters |
| `ActionResult` | Lifecycle status, feedback, error or uncertainty |
| `ObservationEvent` | Time-stamped physical-world evidence ready for upstream ingestion |

These are domain concepts, **not yet finalized schemas**.

## Architectural principles

- Local-first device operation; remote access is optional and deliberately secured.
- Reuse mature device infrastructure rather than reimplementing protocols.
- Separate intent/planning from physical capability and actuation.
- Use open, replaceable adapters; Home Assistant is the first adapter, not a permanent platform lock-in.
- Distinguish *command sent* from *state observed*.
- Require authorization for actuation; hazardous operations need stronger controls.
- Redact private identifiers and credentials before public commits.
- Track architecture decisions in small ADRs rather than rewriting history.

## Interfaces to define next

- Capability inventory and area/entity naming conventions.
- Read-only state/query API and freshness semantics.
- Action request, authorization and result envelopes.
- Event handoff to Context Layer, with provenance and timestamps.
- Test harness for partially connected / unreliable devices.
