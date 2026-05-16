from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from agri_agent_mesh.models import ActionRequest, PolicyDecision, RiskLevel


class SafetyPolicyEngine:
    def __init__(self, policy_path: str | Path = "configs/policies/safety_policy.yaml") -> None:
        self.policy_path = Path(policy_path)
        self.policy = yaml.safe_load(self.policy_path.read_text()) if self.policy_path.exists() else {}

    def evaluate_action(self, action: ActionRequest, context: dict[str, Any] | None = None) -> PolicyDecision:
        context = context or {}
        hard_blocks = self.policy.get("hard_blocks", {})
        require_approval = set(self.policy.get("require_human_approval", []))
        blocked_by: list[str] = []

        if context.get("emergency_stop_active"):
            blocked_by.append("emergency_stop_active")

        if action.action.startswith("uav."):
            max_wind = hard_blocks.get("max_wind_speed_mps_for_uav")
            if max_wind is not None and context.get("wind_speed_mps", 0) > max_wind:
                blocked_by.append("wind_speed_above_uav_limit")
            max_precip = hard_blocks.get("max_precipitation_mm_hr_for_uav")
            if max_precip is not None and context.get("precipitation_mm_hr", 0) > max_precip:
                blocked_by.append("precipitation_above_uav_limit")

        if action.action.startswith("sprayer."):
            max_spray_wind = hard_blocks.get("no_spray_when_wind_mps_above")
            if max_spray_wind is not None and context.get("wind_speed_mps", 0) > max_spray_wind:
                blocked_by.append("wind_speed_above_spray_limit")

        if action.risk_level in {RiskLevel.high, RiskLevel.critical}:
            action.requires_approval = True

        requires_human = action.requires_approval or action.action in require_approval
        if blocked_by:
            return PolicyDecision(
                allowed=False,
                reason="Action blocked by safety policy.",
                requires_human_approval=requires_human,
                blocked_by=blocked_by,
            )

        return PolicyDecision(
            allowed=not requires_human,
            reason="Allowed for autonomous execution." if not requires_human else "Human approval required.",
            requires_human_approval=requires_human,
            blocked_by=[],
        )
