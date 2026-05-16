# API Overview

Start the API:

```bash
make api
```

Open Swagger:

```text
http://localhost:8080/docs
```

Core endpoints:

- `GET /health`
- `GET /agents`
- `GET /agents/{agent_id}`
- `POST /telemetry`
- `GET /telemetry`
- `POST /missions`
- `POST /actions/evaluate`

## Example telemetry

```json
{
  "tenant_id": "demo-tenant",
  "farm_id": "demo-farm",
  "field_id": "field-north",
  "device_id": "soil-001",
  "metric": "soil_moisture",
  "value": 0.17,
  "unit": "m3/m3"
}
```

## Example mission

```json
{
  "tenant_id": "demo-tenant",
  "farm_id": "demo-farm",
  "field_id": "field-north",
  "mission_type": "uav_multispectral_scouting",
  "target": {"device_id": "uav-001", "plot_grid": {"rows": 12, "cols": 8}},
  "constraints": {"wind_speed_mps": 2.5, "precipitation_mm_hr": 0.0},
  "required_capabilities": ["mission.plan", "mission.validate_weather"],
  "risk_level": "high",
  "requires_human_approval": true
}
```
