from __future__ import annotations

from typing import Any

from agri_agent_mesh.config import Settings
from agri_agent_mesh.llm.base import LLMClient


class OpenAIAdapter(LLMClient):
    def __init__(self, settings: Settings) -> None:
        self.settings = settings

    async def complete(self, system: str, user: str, tools: list[dict[str, Any]] | None = None) -> str:
        from openai import AsyncOpenAI

        client = AsyncOpenAI(api_key=self.settings.openai_api_key)
        response = await client.responses.create(
            model=self.settings.openai_model,
            input=[
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            tools=tools or [],
        )
        return response.output_text
