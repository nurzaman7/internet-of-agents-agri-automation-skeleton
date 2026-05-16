from __future__ import annotations

from typing import Any

import httpx

from agri_agent_mesh.config import Settings
from agri_agent_mesh.llm.base import LLMClient


class LocalAdapter(LLMClient):
    def __init__(self, settings: Settings) -> None:
        self.settings = settings

    async def complete(self, system: str, user: str, tools: list[dict[str, Any]] | None = None) -> str:
        payload = {
            "model": self.settings.local_model_name,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            "tools": tools or [],
        }
        async with httpx.AsyncClient(timeout=60) as client:
            res = await client.post(self.settings.local_model_url, json=payload)
            res.raise_for_status()
            data = res.json()
        return data.get("choices", [{}])[0].get("message", {}).get("content", "")
