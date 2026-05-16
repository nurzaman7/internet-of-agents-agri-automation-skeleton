from agri_agent_mesh.models import TelemetryEvent


def test_telemetry_event_defaults():
    event = TelemetryEvent(
        tenant_id="t1",
        farm_id="f1",
        device_id="soil-001",
        metric="soil_moisture",
        value=0.2,
    )
    assert event.event_id.startswith("tel_")
    assert event.quality == "raw"
