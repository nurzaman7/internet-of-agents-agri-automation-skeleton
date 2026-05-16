from __future__ import annotations

import argparse
import asyncio
import random

import yaml

from agri_agent_mesh.models import TelemetryEvent
from agri_agent_mesh.registry import AgentRegistry
from agri_agent_mesh.agents.field_monitor_agent import FieldMonitorAgent


async def run(profile_path: str) -> None:
    profile = yaml.safe_load(open(profile_path, encoding="utf-8"))
    registry = AgentRegistry()
    card = registry.get("field-monitor-agent") or registry.load()["field-monitor-agent"]
    agent = FieldMonitorAgent(card)

    for device in profile.get("devices", []):
        if device.get("type") != "soil_sensor":
            continue
        event = TelemetryEvent(
            tenant_id=profile["tenant_id"],
            farm_id=profile["farm_id"],
            field_id=device["field_id"],
            device_id=device["device_id"],
            metric="soil_moisture",
            value=round(random.uniform(0.10, 0.35), 3),
            unit="m3/m3",
        )
        decision = await agent.handle(event.model_dump())
        print(decision.model_dump_json(indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--scenario", required=True)
    args = parser.parse_args()
    asyncio.run(run(args.scenario))
