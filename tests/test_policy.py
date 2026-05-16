from agri_agent_mesh.models import ActionRequest, RiskLevel
from agri_agent_mesh.policy.guardrails import SafetyPolicyEngine


def test_uav_launch_blocked_by_wind():
    engine = SafetyPolicyEngine()
    action = ActionRequest(
        tenant_id="t1",
        farm_id="f1",
        target_device_id="uav-001",
        action="uav.launch",
        requested_by="test",
        risk_level=RiskLevel.high,
    )
    decision = engine.evaluate_action(action, {"wind_speed_mps": 9.0, "precipitation_mm_hr": 0.0})
    assert decision.allowed is False
    assert "wind_speed_above_uav_limit" in decision.blocked_by


def test_low_risk_read_only_action_allowed():
    engine = SafetyPolicyEngine()
    action = ActionRequest(
        tenant_id="t1",
        farm_id="f1",
        target_device_id="sensor-001",
        action="sensor.read",
        requested_by="test",
        risk_level=RiskLevel.low,
        requires_approval=False,
    )
    decision = engine.evaluate_action(action, {})
    assert decision.allowed is True
