from typing import Any

from agri_agent_mesh.agents.base import BaseAgent
from agri_agent_mesh.models import ActionRequest, DecisionRecord, MissionRequest, RiskLevel
from agri_agent_mesh.policy.guardrails import SafetyPolicyEngine


class MissionPlannerAgent(BaseAgent):
    def __init__(self, card, policy_engine: SafetyPolicyEngine | None = None) -> None:
        super().__init__(card)
        self.policy_engine = policy_engine or SafetyPolicyEngine()

    async def handle(self, message: dict[str, Any]) -> DecisionRecord:
        mission = MissionRequest(**message)
        action_name = "uav.launch" if mission.mission_type.startswith("uav") else "mission.execute"
        action = ActionRequest(
            tenant_id=mission.tenant_id,
            farm_id=mission.farm_id,
            field_id=mission.field_id,
            target_device_id=mission.target.get("device_id", "unassigned"),
            action=action_name,
            params={"mission_id": mission.mission_id, "target": mission.target},
            requested_by=self.card.id,
            requires_approval=True,
            risk_level=RiskLevel.high,
        )
        policy = self.policy_engine.evaluate_action(action, context=mission.constraints)
        return DecisionRecord(
            agent_id=self.card.id,
            tenant_id=mission.tenant_id,
            farm_id=mission.farm_id,
            mission_id=mission.mission_id,
            rationale="Mission plan created and evaluated against safety policy.",
            confidence=0.7,
            suggested_actions=[action],
            policy_decision=policy,
        )
