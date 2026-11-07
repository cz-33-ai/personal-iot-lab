# PWI Roadmap

> Planned work is **not** a claim of current implementation. Progress is recorded using issues with acceptance criteria and links to evidence.

## Current baseline — already validated

- Local Mosquitto publish/subscribe works.
- Zigbee2MQTT reports motion/light sensor messages over MQTT.
- ESP32-C3 running ESPHome connects to Wi-Fi/MQTT, publishes heartbeat and receives a command.
- Temperature/humidity reporting timing remains an open diagnostic.
- No verified end-to-end, multi-device physical actuation workflow yet.

## M0 — Foundation and project structure

- [x] Establish public documentation repository and private raw lab notebook.
- [x] Define PWI vision, architectural boundaries, publication rules and roadmap.
- [x] Adopt the canonical public repository slug `physical-world-interface`.
- [x] Establish issue conventions, contribution guide, public issue forms and review checklist.
- [ ] Create first architecture decision record (ADR) for Home Assistant integration.

**Exit:** every subsequent milestone has an issue, a measurable acceptance test and an owner.

## M1 — Unified device inventory and read-only perception

- [ ] Deploy Home Assistant in a repeatable development environment.
- [ ] Connect existing MQTT broker and Zigbee2MQTT.
- [ ] Make Zigbee sensors visible with correct entity/area semantics.
- [ ] Decide whether ESPHome uses MQTT or Native API for the prototype.
- [ ] Record device availability, timestamps and state freshness.

**Exit:** read two device states through one consistent interface and demonstrate change propagation.

## M2 — Controlled actuation and feedback

- [ ] Obtain one **confirmed** controllable actuator (e.g. lamp/LED strip/plug), recording exact hardware separately.
- [ ] Command on/off (and brightness if supported) through Home Assistant.
- [ ] Distinguish command dispatch from confirmed state change.
- [ ] Exercise offline/unavailable-device failure and timeout reporting.

**Exit:** reliable action request → dispatch → observable result, including a failure case.

## M3 — Agent-executable environment action

- [ ] Define capability discovery, permissions and action schema.
- [ ] Expose a limited control interface to an external Agent (MCP or API, selected by testing).
- [ ] Implement “Prepare for Sleep” using only connected capabilities, with unavailable features reported explicitly.
- [ ] Support personal preference parameters supplied by the Personal Context Layer.

**Exit:** a test intent produces an auditable plan, authorized actions and per-device result summary.

## M4 — Physical-world context event handoff

- [ ] Define normalized observation and action-outcome events.
- [ ] Connect events to the **existing** Personal Agent Platform ingestion boundary.
- [ ] Preserve source, timestamps, confidence/uncertainty and valid state.
- [ ] Demonstrate that physical events can inform later requests without duplicating a memory system inside PWI.

**Exit:** one event from a device and one result from an action are ingestible through a documented contract.

## M5 — Reliability, security, portability

- [ ] Standardize local configuration and backups, with credentials excluded.
- [ ] Verify network isolation, least-privilege access and recovery after restart.
- [ ] Add automated tests and CI checks for examples/contracts.
- [ ] Keep services portable to an always-on host.

## Curriculum track (parallel)

Turn **verified** experiments into lessons with concept, architecture, equipment, hands-on steps, expected/actual results, troubleshooting, exercises and grading criteria. See [course plan](course-plan.md).

## Working rule

For each task, keep: **Goal → Design → Implementation → Evidence → Acceptance → Learning → Public Release Review**.


## Current tracked implementation issues

| Work item | GitHub Issue |
|---|---|
| M1: Home Assistant + Mosquitto + Zigbee2MQTT | [#1](https://github.com/cz-33-ai/physical-world-interface/issues/1) |
| M1 research: ESPHome Native API vs MQTT | [#2](https://github.com/cz-33-ai/physical-world-interface/issues/2) |
| M2: First controllable actuator and feedback | [#3](https://github.com/cz-33-ai/physical-world-interface/issues/3) |
| M3: Prepare for Sleep | [#4](https://github.com/cz-33-ai/physical-world-interface/issues/4) |
| M4: Observation and action-outcome contracts | [#5](https://github.com/cz-33-ai/physical-world-interface/issues/5) |


## Reproducibility and community

- [x] Publish an offline, dependency-free simulated demonstration and tests.
- [x] Link a developer [Quick Start](../QUICKSTART.md) from the README.
- [ ] Confirm at least one **independent external reproduction** with feedback.
- [ ] Replace simulator-only claims with a genuine connected-hardware demo after M2.
- [ ] Publish a short, accurate demo video and accompanying instructions once verified.

See [community release gates](community/launch-plan.md) and the [flagship demo plan](demos/prepare-for-sleep.md).
