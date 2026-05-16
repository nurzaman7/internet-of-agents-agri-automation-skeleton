from typing import Any

from agri_agent_mesh.agents.base import BaseAgent
from agri_agent_mesh.models import CarbonEvent


class CarbonAgent(BaseAgent):
    async def estimate_from_activity(self, message: dict[str, Any]) -> CarbonEvent:
        # Replace with your audited factor tables and local methodology.
        quantity = float(message.get("activity_quantity", 0.0))
        factor = float(message.get("emission_factor", 1.0))
        return CarbonEvent(
            tenant_id=message["tenant_id"],
            farm_id=message["farm_id"],
            field_id=message.get("field_id"),
            source_type=message.get("source_type", "unknown_activity"),
            gas=message.get("gas", "co2e"),
            quantity=quantity * factor,
            unit=message.get("output_unit", "kg_co2e"),
            scope=message.get("scope", "scope_1"),
            factor_id=message.get("factor_id"),
            metadata={"activity_quantity": quantity, "emission_factor": factor},
        )

    async def handle(self, message: dict[str, Any]) -> dict[str, Any]:
        event = await self.estimate_from_activity(message)
        return event.model_dump(mode="json")
