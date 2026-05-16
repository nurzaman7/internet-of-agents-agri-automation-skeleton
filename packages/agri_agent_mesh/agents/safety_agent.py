from typing import Any

from agri_agent_mesh.agents.base import BaseAgent
from agri_agent_mesh.models import ActionRequest
from agri_agent_mesh.policy.guardrails import SafetyPolicyEngine


class SafetyAgent(BaseAgent):
    def __init__(self, card, policy_engine: SafetyPolicyEngine | None = None) -> None:
        super().__init__(card)
        self.policy_engine = policy_engine or SafetyPolicyEngine()

    async def handle(self, message: dict[str, Any]) -> dict[str, Any]:
        action = ActionRequest(**message["action"] if "action" in message else message)
        context = message.get("context", {})
        decision = self.policy_engine.evaluate_action(action, context)
        return decision.model_dump(mode="json")
