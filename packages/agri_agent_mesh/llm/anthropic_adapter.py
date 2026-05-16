from __future__ import annotations

from typing import Any

from agri_agent_mesh.config import Settings
from agri_agent_mesh.llm.base import LLMClient


class AnthropicAdapter(LLMClient):
    def __init__(self, settings: Settings) -> None:
        self.settings = settings

    async def complete(self, system: str, user: str, tools: list[dict[str, Any]] | None = None) -> str:
        import anthropic

        client = anthropic.AsyncAnthropic(api_key=self.settings.anthropic_api_key)
        response = await client.messages.create(
            model=self.settings.anthropic_model,
            max_tokens=1500,
            system=system,
            messages=[{"role": "user", "content": user}],
            tools=tools or [],
        )
        return "".join(block.text for block in response.content if getattr(block, "type", None) == "text")
