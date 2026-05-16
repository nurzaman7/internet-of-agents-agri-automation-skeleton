import json
import signal
import time
from pathlib import Path

import structlog

from agri_agent_mesh.config import get_settings
from agri_agent_mesh.connectors.mqtt_bus import MQTTBus
from agri_agent_mesh.observability.logging import configure_logging

RUNNING = True


def stop(*_args):
    global RUNNING
    RUNNING = False


def main() -> None:
    settings = get_settings()
    configure_logging(settings.log_level)
    log = structlog.get_logger()
    signal.signal(signal.SIGINT, stop)
    signal.signal(signal.SIGTERM, stop)

    bus = MQTTBus(settings)
    bus.connect()
    log.info("edge_agent_started", mqtt_host=settings.mqtt_host, mqtt_port=settings.mqtt_port)

    demo_path = Path("examples/field-crop-carbon/farm_profile.yaml")
    while RUNNING:
        payload = {
            "tenant_id": "demo-tenant",
            "farm_id": "demo-farm",
            "field_id": "field-north",
            "device_id": "soil-001",
            "metric": "soil_moisture",
            "value": 0.21,
            "unit": "m3/m3",
            "metadata": {"profile": str(demo_path)},
        }
        bus.publish_json("agri/demo-farm/telemetry", payload)
        log.info("edge_telemetry_published", payload=json.dumps(payload))
        time.sleep(15)


if __name__ == "__main__":
    main()
