from typing import Any

from agri_agent_mesh.agents.base import BaseAgent
from agri_agent_mesh.models import DecisionRecord, TelemetryEvent


class FieldMonitorAgent(BaseAgent):
    async def handle(self, message: dict[str, Any]) -> DecisionRecord:
        event = TelemetryEvent(**message)
        anomaly = False
        rationale = f"Telemetry {event.metric}={event.value}{event.unit or ''} observed."

        if event.metric in {"soil_moisture", "soil_water_content"} and float(event.value) < 0.18:
            anomaly = True
            rationale = "Low soil moisture detected; irrigation review recommended."
        if event.metric == "wind_speed" and float(event.value) > 5.0:
            anomaly = True
            rationale = "High wind detected; UAV and spraying operations should be reviewed."

        return DecisionRecord(
            agent_id=self.card.id,
            tenant_id=event.tenant_id,
            farm_id=event.farm_id,
            input_ref=event.event_id,
            rationale=rationale,
            confidence=0.75 if anomaly else 0.55,
        )
