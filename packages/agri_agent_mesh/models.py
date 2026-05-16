from __future__ import annotations

from datetime import datetime, timezone
from enum import Enum
from typing import Any, Literal
from uuid import uuid4

from pydantic import BaseModel, Field


def utcnow() -> datetime:
    return datetime.now(timezone.utc)


class RiskLevel(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"
    critical = "critical"


class AgentRole(str, Enum):
    monitor = "monitor"
    mission_planner = "mission_planner"
    operations = "operations"
    safety = "safety"
    sustainability = "sustainability"
    reporting = "reporting"


class AgentCard(BaseModel):
    id: str
    name: str
    version: str = "0.1.0"
    role: str
    runs_on: list[str] = Field(default_factory=list)
    description: str = ""
    capabilities: list[str] = Field(default_factory=list)
    tools: list[str] = Field(default_factory=list)
    inputs: list[str] = Field(default_factory=list)
    outputs: list[str] = Field(default_factory=list)
    risk_level: RiskLevel = RiskLevel.low
    auth_scopes: list[str] = Field(default_factory=list)
    requires_human_approval: bool = False
    endpoint: str | None = None
    metadata: dict[str, Any] = Field(default_factory=dict)


class TelemetryEvent(BaseModel):
    event_id: str = Field(default_factory=lambda: f"tel_{uuid4().hex}")
    tenant_id: str
    farm_id: str
    field_id: str | None = None
    device_id: str
    metric: str
    value: float | int | str | bool
    unit: str | None = None
    timestamp: datetime = Field(default_factory=utcnow)
    location: dict[str, Any] | None = None
    quality: Literal["raw", "validated", "estimated", "suspect"] = "raw"
    metadata: dict[str, Any] = Field(default_factory=dict)


class MissionRequest(BaseModel):
    mission_id: str = Field(default_factory=lambda: f"mis_{uuid4().hex}")
    tenant_id: str
    farm_id: str
    field_id: str | None = None
    mission_type: str
    target: dict[str, Any]
    constraints: dict[str, Any] = Field(default_factory=dict)
    required_capabilities: list[str] = Field(default_factory=list)
    risk_level: RiskLevel = RiskLevel.medium
    requires_human_approval: bool = False
    created_at: datetime = Field(default_factory=utcnow)


class ActionRequest(BaseModel):
    request_id: str = Field(default_factory=lambda: f"act_{uuid4().hex}")
    tenant_id: str
    farm_id: str
    field_id: str | None = None
    target_device_id: str
    action: str
    params: dict[str, Any] = Field(default_factory=dict)
    requested_by: str
    requires_approval: bool = True
    risk_level: RiskLevel = RiskLevel.high
    timestamp: datetime = Field(default_factory=utcnow)


class PolicyDecision(BaseModel):
    allowed: bool
    reason: str
    requires_human_approval: bool = False
    blocked_by: list[str] = Field(default_factory=list)
    evaluated_at: datetime = Field(default_factory=utcnow)


class DecisionRecord(BaseModel):
    decision_id: str = Field(default_factory=lambda: f"dec_{uuid4().hex}")
    agent_id: str
    tenant_id: str
    farm_id: str
    mission_id: str | None = None
    input_ref: str | None = None
    rationale: str
    confidence: float = Field(ge=0.0, le=1.0)
    suggested_actions: list[ActionRequest] = Field(default_factory=list)
    policy_decision: PolicyDecision | None = None
    created_at: datetime = Field(default_factory=utcnow)


class CarbonEvent(BaseModel):
    event_id: str = Field(default_factory=lambda: f"car_{uuid4().hex}")
    tenant_id: str
    farm_id: str
    field_id: str | None = None
    source_type: str
    gas: Literal["co2", "ch4", "n2o", "co2e"]
    quantity: float
    unit: str
    scope: Literal["scope_1", "scope_2", "scope_3", "biogenic"]
    method: str = "activity_factor"
    factor_id: str | None = None
    timestamp: datetime = Field(default_factory=utcnow)
    metadata: dict[str, Any] = Field(default_factory=dict)
