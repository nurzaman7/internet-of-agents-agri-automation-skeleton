from pathlib import Path
import yaml

from agri_agent_mesh.models import AgentCard


class AgentRegistry:
    def __init__(self, config_dir: str | Path = "configs/agents") -> None:
        self.config_dir = Path(config_dir)
        self._agents: dict[str, AgentCard] = {}

    def load(self) -> dict[str, AgentCard]:
        self._agents.clear()
        for path in sorted(self.config_dir.glob("*.yaml")):
            data = yaml.safe_load(path.read_text())
            card = AgentCard(**data)
            self._agents[card.id] = card
        return self._agents

    def list(self) -> list[AgentCard]:
        if not self._agents:
            self.load()
        return list(self._agents.values())

    def find_by_capability(self, capability: str) -> list[AgentCard]:
        return [agent for agent in self.list() if capability in agent.capabilities]

    def get(self, agent_id: str) -> AgentCard | None:
        if not self._agents:
            self.load()
        return self._agents.get(agent_id)
