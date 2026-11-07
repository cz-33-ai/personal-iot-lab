# GitHub Project Workflow

## Repository roles

- **Public: `physical-world-interface` (PWI)** — project vision, architecture, contracts, reusable code/config examples, verified tutorials, course lessons, issues and releases.
- **Private: `smart-home-lab`** — raw chronological lab journal, exact Terminal commands, observed output, troubleshooting, screenshots/evidence and internal experimental notes.
- **Private: `personal-agent-platform`** — authoritative high-level Personal Agent Platform architecture and shared platform boundaries. PWI must remain consistent with it; do not duplicate or silently revise its approved design.

PWI's public repository has been renamed to `physical-world-interface`. Keep private experiment evidence separate; do not migrate raw private records into the public repository.

## Source of truth

| Material | Authoritative home |
|---|---|
| Approved overall Personal Agent architecture | `personal-agent-platform` |
| PWI subsystem architecture and capability contracts | Public PWI repository |
| Raw hardware/network experiments and evidence | Private smart-home-lab |
| Sanitized, repeatable lessons and examples | Public PWI repository |
| Open work, bugs, experiments, decisions | Public GitHub Issues unless private details are required |

## Issues

Each issue contains:
- Problem / intended result
- Scope and dependencies
- Acceptance criteria that can be tested
- Evidence link or reproduction steps
- Privacy/security considerations if relevant

Suggested issue categories: `architecture`, `experiment`, `hardware`, `integration`, `control`, `perception`, `context-handoff`, `curriculum`, `bug`, `security`.

Issue categories are conventions; GitHub labels can be created later.

## Branches, Pull Requests and milestones

- Protect `main` for tested and reviewed changes when branch protection is configured.
- Use concise branches, e.g. `feat/ha-mqtt-integration`, `docs/device-contract`, `lab/ts0201-reporting`.
- Changes to interfaces or hardware behavior should explain assumptions, tests, and known limitations in the PR.
- A milestone is complete only when acceptance criteria are supported by evidence.
- Don't claim a physical command succeeded without confirmation/feedback.
- Use ADRs for important trade-offs (Home Assistant as hub, MQTT vs Native API, agent control boundary, device identity, data retention).
- Publish version tags for actual usable capabilities, not just README revisions.

## Experiments → reusable features → course lessons

1. Prototype in a controlled lab.
2. Capture exact observations and errors in the private journal.
3. Extract a tested example/config with no secrets.
4. Define a repeatable test or acceptance checklist.
5. Publish sanitized technical documentation in the PWI repo.
6. Translate validated work into a lesson with exercises.

## Release safety

Before every public commit or PR:
- Ensure no credentials, access tokens, private keys or secret files.
- Remove SSIDs, private IP assignments, MAC/IEEE identifiers, serial numbers and sensitive household labels from logs/screenshots.
- Avoid exposing device inventories and security configurations that identify the actual home.
- Prefer placeholders and example configs.
- Review current changes **and Git history**. Removing a secret from the latest commit alone does not erase it from history.
- Never push unreviewed raw lab captures to the public repository.

The public repository is not a copy of the private one. Publication is an explicit review step.


## First-time contributors

Start at [QUICKSTART](../QUICKSTART.md), which requires no hardware. The small offline simulator is a real runnable example with unit tests, **not** real physical actuation. Use the [reproducibility issue form](https://github.com/cz-33-ai/physical-world-interface/issues/new/choose) for sanitized external feedback.

For project maintainers, [Mission Control](../START_HERE.md) is the current task dashboard, while Issues are the canonical per-task progress records.

## Release gates

Use [the open-source launch plan](community/launch-plan.md) to distinguish three different milestones:
1. A stranger can reproduce the offline teaching example.
2. A physical actuator is verified with real state feedback.
3. The actual Agent intent → multi-device outcomes → context event path is demonstrated.

Do not claim gates 2 or 3 before the linked acceptance criteria pass.
