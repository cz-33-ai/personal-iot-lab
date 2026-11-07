# Contributing to Physical World Interface

Thanks for your interest in PWI. We are building a **public, reproducible interface between Personal Agents and physical-world capabilities**, starting with local IoT.

> **License:** PWI is licensed under the [Apache License 2.0](LICENSE). By contributing, you agree to make your contributions available under that license and confirm you have the rights needed to submit them. Preserve license, copyright and any applicable NOTICE files when redistributing; identify modified files when required. Do not copy third-party code or assets unless their licenses permit it.

## A good first contribution

- Reproduce the [zero-hardware simulator](QUICKSTART.md) and report a clear issue with OS/Python version and sanitized output.
- Improve a command explanation or troubleshoot a reproducibility gap in a [hands-on experiment](docs/01-mqtt-broker-and-lan-test.md).
- Add a test for missing capabilities, unavailable devices or stale state.
- Propose a better device/action contract with explicit failure semantics.
- Suggest an improvement to the [course plan](docs/course-plan.md).

## Development without hardware

```bash
git clone https://github.com/cz-33-ai/physical-world-interface.git
cd physical-world-interface
python3 -m unittest discover -s tests -v
python3 examples/prepare_for_sleep_simulator.py --apply --scenario offline
```

The demo is intentionally offline and dependency-free. It does not operate any real IoT device.

## Before opening a pull request

1. Open an Issue for substantial architectural or behavior changes.
2. Keep the patch focused, and state which acceptance criterion it addresses.
3. Provide actual test results or label the content **proposal / unverified**.
4. Do not change the approved top-level Personal Agent Platform architecture as part of a PWI documentation PR.
5. Follow the [GitHub workflow](docs/project-workflow.md) and PR checklist.

## Strict public privacy rules

Never commit real credentials, tokens, passwords, Zigbee keys, private network addresses, SSIDs, MAC / IEEE addresses, identifying room/device names, or unreviewed screenshots/terminal logs. Mock examples must use generic names and invented states.

A private repository exists for raw experimentation; do not upload or link private evidence here. If a secret has entered public Git history, rotating/revoking it is more important than simply deleting the latest file.

## Device control and safety

- Do not expose an unauthenticated MQTT broker to the public Internet.
- Use least-privilege physical device control and explicit authorization boundaries.
- Distinguish **requested**, **dispatched**, **confirmed**, **failed**, and **unverified**.
- Keep hazardous mains wiring and safety-critical actuation out of starter examples.
- Mark mock/simulated outcomes in every demo and screenshot.

## How we evaluate contributions

**Reproducibility > novelty.** We especially value complete instructions, demonstrated hardware feedback, clear errors, accessible explanations and small tests that prevent regression.

PWI aims to grow into both an open-source reference platform and an educational curriculum. Great contributions should help a new learner understand not just *what* to type, but *why* it works.
