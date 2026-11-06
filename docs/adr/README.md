# Architecture Decision Records (ADRs)

Use one immutable, numbered markdown file per consequential engineering decision.

## Suggested format

- Title / Status: Proposed, Accepted, Superseded
- Context and goal
- Decision
- Considered alternatives
- Rationale and trade-offs
- Consequences / security implications
- Evidence, date and links

## Initial decisions to evaluate

1. Home Assistant as the first physical device hub.
2. ESPHome Native API versus MQTT for Home Assistant-managed ESP32 nodes.
3. The Agent-to-PWI semantic capability interface (MCP and/or API).
4. Command acknowledgement versus observed state confirmation.
5. Event schema and handoff to the Personal Context Layer.

**No decision is accepted by virtue of appearing on this proposed list.**
