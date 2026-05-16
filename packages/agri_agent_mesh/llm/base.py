from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class LLMClient(ABC):
    @abstractmethod
    async def complete(self, system: str, user: str, tools: list[dict[str, Any]] | None = None) -> str:
        raise NotImplementedError
