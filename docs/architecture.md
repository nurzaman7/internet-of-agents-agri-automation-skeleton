# Architecture

AgriAgentMesh separates the agricultural automation stack into four cooperating planes.

## 1. Field plane

The field plane contains sensors, actuators, UAVs, robots, field vehicles, cameras, weather stations, carbon monitoring devices, pumps, valves, and machinery telemetry. The field plane should continue operating safely even when cloud connectivity is unavailable.

Supported adapter patterns:

- MQTT sensors
- LoRaWAN network server webhooks
- 6LoWPAN gateways
- Modbus and OPC-UA industrial devices
- MAVLink UAVs
- ROS2 robots
- CAN bus or fleet APIs for vehicles
- REST/gRPC vendor APIs

## 2. Edge plane

The edge plane provides local buffering, fast decisions, and safety enforcement close to hardware. It runs on an industrial PC, Jetson, Raspberry Pi, or gateway.

Core services:

- `apps/edge-agent`
- local MQTT client or broker
- offline queue
- local policy checks
- optional image, sensor, and carbon preprocessing
- command relay to hardware connectors

## 3. Cloud plane

The cloud plane coordinates multi-agent workflows, storage, dashboards, APIs, and long-horizon analytics.

Core services:

- `apps/api`
- `apps/orchestrator`
- Postgres for relational metadata
- time-series database for telemetry
- object storage for images and maps
- Redis for queues and coordination
- observability stack for logs, metrics, traces, and audit events

## 4. Agent communication plane

This is the reusable layer that makes the system an Internet of Agents instead of a collection of scripts.

Each agent declares:

- identity,
- capabilities,
- tools,
- input/output contracts,
- risk level,
- authorization scopes,
- runtime location,
- whether it can perform or only recommend actions.

The orchestrator resolves which agent should handle a task, passes only the required context, records decisions, and enforces approval and safety policy before any physical action.

## Message topics

Suggested MQTT topic pattern:

```text
agri/{farm_id}/telemetry
agri/{farm_id}/events/anomaly
agri/{farm_id}/missions/requested
agri/{farm_id}/missions/status
agri/{farm_id}/actions/requested
agri/{farm_id}/actions/approved
agri/{farm_id}/actions/executed
agri/{farm_id}/audit
```

## Data contracts

Use the JSON schemas in `schemas/` as the public contract. Avoid coupling an agent to another agent's internal memory, private prompts, or implementation details.

## Production principles

- Design for intermittent connectivity.
- Keep edge actions deterministic and auditable.
- Treat AI outputs as recommendations until approved.
- Use per-tool authorization and least privilege.
- Keep hardware adapters small, testable, and replaceable.
- Store every decision that affects field operations.
- Make all integrations optional and replaceable.
