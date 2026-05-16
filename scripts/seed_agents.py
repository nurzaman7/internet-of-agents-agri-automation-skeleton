from agri_agent_mesh.registry import AgentRegistry

registry = AgentRegistry()
agents = registry.load()
print(f"Loaded {len(agents)} agents:")
for agent_id, card in agents.items():
    print(f"- {agent_id}: {', '.join(card.capabilities)}")
