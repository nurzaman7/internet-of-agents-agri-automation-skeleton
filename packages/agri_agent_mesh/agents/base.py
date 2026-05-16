from __future__ import annotations

from typing import Any, Protocol

from agri_agent_mesh.models import AgentCard, DecisionRecord


class AgentRuntime(Protocol):
    card: AgentCard

    async def handle(self, message: dict[str, Any]) -> DecisionRecord | dict[str, Any]:
        ...


class BaseAgent:
    def __init__(self, card: AgentCard) -> None:
        self.card = card

    def can_handle(self, capability: str) -> bool:
        return capability in self.card.capabilities

    async def handle(self, message: dict[str, Any]) -> dict[str, Any]:
        return {
            "agent_id": self.card.id,
            "status": "accepted",
            "message": message,
            "note": "Override handle() in a concrete agent.",
        }
