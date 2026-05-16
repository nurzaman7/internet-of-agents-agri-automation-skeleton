# Security and Safety

## Baseline controls

- Use TLS for all cloud and remote edge communication.
- Use MQTT over TLS in production.
- Use OAuth2/OIDC or mTLS for service identity.
- Use short-lived credentials for agents.
- Use least privilege scopes from agent cards.
- Keep all physical action tools behind the policy engine.
- Require approval for high-risk actions.
- Store immutable audit records for decisions and commands.

## Prompt injection and connector risk

When an agent can use tools or MCP connectors, external content may contain malicious instructions. Do not let tool output override safety policy, authentication, or physical operation limits.

Required mitigations:

- tool allowlists,
- human approval for sensitive actions,
- output validation with schemas,
- trusted connector endpoints,
- audit logs for data sent to third-party services,
- read-only default permissions,
- sandboxing for code execution,
- separation between observation and actuation tools.

## Physical operation safety

Never rely on LLM output alone for physical control. Use deterministic validation for:

- geofence,
- wind and precipitation,
- chemical application windows,
- vehicle operating area,
- equipment health,
- battery and fuel levels,
- emergency stop,
- human/operator approval.
