# Complete build prompt for an AI coding agent

Use this prompt when asking a coding agent to implement or extend this repository.

```text
You are a principal platform engineer building AgriAgentMesh, a production-level Internet of Agents skeleton for agriculture.

Build a reusable open-source repository that lets users automate agricultural monitoring and operations across cloud, edge, and field components. The system must support wireless sensor modules, UAVs, robots, field vehicles, irrigation and pump actuators, carbon monitoring devices, weather stations, image processing pipelines, and human operators.

Core goal:
Create an interoperable agent mesh where agents can discover capabilities, exchange structured messages, call tools, use OpenAI or Anthropic Claude or a local model, connect to external systems through MCP-style connectors, and safely automate or recommend agricultural workflows.

Architecture requirements:
1. Field layer: sensors, UAVs, robots, vehicles, actuators, weather station, carbon devices.
2. Edge layer: gateway runtime, MQTT, local safety policy, offline queue, local preprocessing, connector adapters, emergency-stop handling.
3. Cloud layer: REST API, agent orchestrator, agent registry, workflow state, Postgres, time-series storage, object storage, dashboard-ready APIs, audit logs.
4. AI and connector layer: OpenAI adapter, Anthropic adapter, local-model adapter, MCP connector scaffolding, function/tool schema support.
5. Security layer: OAuth/JWT-ready auth, least-privilege agent scopes, TLS, tool allowlists, human approval for sensitive actions.
6. Observability layer: structured logs, metrics-ready design, audit records, decision records, trace IDs.

Implement these reusable agents:
- field-monitor-agent: consumes telemetry and detects field anomalies.
- uav-mission-agent: plans UAV missions, validates weather/geofence, requests approval.
- robot-ops-agent: coordinates scouting or sampling robots through a connector interface.
- vehicle-agent: tracks field vehicles and suggests routing/task optimization.
- irrigation-agent: recommends irrigation actions and optionally triggers valves after policy approval.
- carbon-agent: converts fuel, fertilizer, energy, soil, livestock, and sensor activity into carbon events with traceable factor IDs.
- safety-agent: enforces policy before any physical operation.
- report-agent: generates reusable operator, grower, researcher, and carbon reports.

Production requirements:
- Python 3.11+, FastAPI, Pydantic v2, Docker Compose, Kubernetes starter manifests.
- JSON schemas for AgentCard, TelemetryEvent, MissionRequest, ActionRequest, DecisionRecord, CarbonEvent.
- Provider abstraction for OpenAI, Anthropic, and local model endpoints.
- Strict separation of recommendation, approval, and execution.
- No direct physical action without deterministic policy checks.
- Every decision must produce an auditable DecisionRecord.
- All connectors must have timeouts, retries, and simulated test mode.
- Edge runtime must tolerate cloud disconnection and queue events locally.
- Build examples that users can modify for their own farm profile.

Deliverables:
- Repository tree with apps/, packages/, configs/, docs/, examples/, schemas/, prompts/, k8s/, scripts/, tests/.
- README with quickstart and reuse guide.
- Docker Compose for Postgres, Redis, MQTT, MinIO, API, and orchestrator.
- API endpoints: /health, /agents, /telemetry, /missions, /actions/evaluate.
- Agent configs in YAML.
- Safety policy YAML.
- Example farm profile YAML.
- Unit tests for schemas and safety policy.
- CI workflow for lint and tests.
- Clear TODO markers where users should plug in vendor-specific hardware APIs.

Implementation style:
- Keep the skeleton clean, typed, and easy to extend.
- Prefer small interfaces over large frameworks.
- Use provider-neutral names and avoid coupling to any one hardware vendor or AI model.
- Document how users can add an agent, connector, policy, and farm profile.
```
```
