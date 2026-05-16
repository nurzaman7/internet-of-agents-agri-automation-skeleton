import asyncio
import structlog

from agri_agent_mesh.config import get_settings
from agri_agent_mesh.llm.factory import make_llm_client
from agri_agent_mesh.observability.logging import configure_logging
from agri_agent_mesh.registry import AgentRegistry

SYSTEM = """You are the AgriAgentMesh cloud orchestrator. Route tasks to specialized agents, prefer safe recommendations over direct physical actions, and require explicit approval for high-risk operations."""


async def main() -> None:
    settings = get_settings()
    configure_logging(settings.log_level)
    log = structlog.get_logger()
    registry = AgentRegistry()
    agents = registry.load()
    log.info("orchestrator_started", agents=list(agents.keys()), provider=settings.llm_provider)

    # Optional smoke test for configured LLM. Disabled by default to avoid API calls on startup.
    if False:
        llm = make_llm_client()
        answer = await llm.complete(SYSTEM, "Summarize active agent capabilities.")
        log.info("llm_answer", answer=answer)

    while True:
        await asyncio.sleep(30)
        log.info("orchestrator_heartbeat", agents=len(agents))


if __name__ == "__main__":
    asyncio.run(main())
