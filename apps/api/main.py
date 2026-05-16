from fastapi import FastAPI, HTTPException

from agri_agent_mesh.config import get_settings
from agri_agent_mesh.models import ActionRequest, MissionRequest, TelemetryEvent
from agri_agent_mesh.policy.guardrails import SafetyPolicyEngine
from agri_agent_mesh.registry import AgentRegistry
from agri_agent_mesh.storage.repository import InMemoryRepository

settings = get_settings()
app = FastAPI(title=settings.project_name, version="0.1.0")
registry = AgentRegistry()
repo = InMemoryRepository()
policy_engine = SafetyPolicyEngine()


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "project": settings.project_name, "environment": settings.environment}


@app.get("/agents")
def list_agents() -> list[dict]:
    return [agent.model_dump(mode="json") for agent in registry.list()]


@app.get("/agents/{agent_id}")
def get_agent(agent_id: str) -> dict:
    agent = registry.get(agent_id)
    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")
    return agent.model_dump(mode="json")


@app.post("/telemetry")
def ingest_telemetry(event: TelemetryEvent) -> dict:
    return repo.add("telemetry", event.model_dump(mode="json"))


@app.get("/telemetry")
def list_telemetry() -> list[dict]:
    return repo.list("telemetry")


@app.post("/missions")
def create_mission(mission: MissionRequest) -> dict:
    repo.add("missions", mission.model_dump(mode="json"))
    matching_agents = registry.find_by_capability("mission.plan")
    return {"mission": mission.model_dump(mode="json"), "candidate_agents": [a.id for a in matching_agents]}


@app.post("/actions/evaluate")
def evaluate_action(action: ActionRequest, context: dict | None = None) -> dict:
    decision = policy_engine.evaluate_action(action, context or {})
    return decision.model_dump(mode="json")
