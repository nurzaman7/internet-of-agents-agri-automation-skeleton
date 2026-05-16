from __future__ import annotations

from typing import Any


class InMemoryRepository:
    def __init__(self) -> None:
        self.telemetry: list[dict[str, Any]] = []
        self.decisions: list[dict[str, Any]] = []
        self.missions: list[dict[str, Any]] = []
        self.carbon_events: list[dict[str, Any]] = []

    def add(self, collection: str, item: dict[str, Any]) -> dict[str, Any]:
        getattr(self, collection).append(item)
        return item

    def list(self, collection: str) -> list[dict[str, Any]]:
        return list(getattr(self, collection))
