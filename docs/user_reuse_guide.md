# Reuse Guide

AgriAgentMesh is designed so users can adopt only the parts they need.

## For a sensor-only farm monitoring project

1. Keep `field-monitor-agent`, `safety-agent`, and `report-agent`.
2. Disable UAV, robot, and actuation configs.
3. Use MQTT or REST to ingest sensor telemetry.
4. Build dashboards from `/telemetry` and time-series storage.

## For a UAV scouting project

1. Enable `uav-mission-agent`.
2. Add your UAV adapter under `packages/agri_agent_mesh/connectors/equipment.py` or a new module.
3. Add geofence and weather tools.
4. Keep launch and landing in human-approval mode until field validation is complete.
5. Add an edge image-processing service if raw data is large.

## For carbon monitoring

1. Enable `carbon-agent`.
2. Add farm activity sources: fuel, fertilizer, electricity, manure, soil, residue, livestock, transport, and sensor measurements.
3. Replace the demo factor logic with your audited methodology.
4. Store factor IDs and assumptions in every `CarbonEvent`.
5. Generate reports through `report-agent`.

## For robotics and field vehicles

1. Add device records to your farm profile.
2. Add a connector for ROS2, CAN bus, fleet API, or vendor SDK.
3. Require geofence, speed, operator, and emergency stop context.
4. Keep the robot or vehicle agent edge-local for low-latency stop commands.

## How to add a new agent

1. Create `configs/agents/my-agent.yaml`.
2. Implement `packages/agri_agent_mesh/agents/my_agent.py`.
3. Declare capabilities and tool names.
4. Add schemas for new inputs or outputs.
5. Add tests.
6. Register any sensitive action in `configs/policies/safety_policy.yaml`.

## How to add a connector

1. Create a connector module under `packages/agri_agent_mesh/connectors/`.
2. Keep credentials in environment variables or a secrets manager.
3. Provide a small typed interface.
4. Log request IDs, but avoid logging secrets.
5. Add retries and timeouts.
6. Add a simulator for local tests.
