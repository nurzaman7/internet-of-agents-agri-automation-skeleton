from agri_agent_mesh.registry import AgentRegistry


def test_registry_loads_bundled_agent_cards():
    registry = AgentRegistry()
    agents = registry.load()
    assert {"field-monitor-agent", "uav-mission-agent", "carbon-agent", "safety-agent"} <= set(agents)


def test_registry_lookup_helpers():
    registry = AgentRegistry()
    assert registry.get("field-monitor-agent") is not None
    assert registry.get("no-such-agent") is None
    assert len(registry.list()) == len(registry.load())
    for card in registry.list():
        for capability in card.capabilities:
            assert card in registry.find_by_capability(capability)
