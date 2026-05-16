from __future__ import annotations

from dataclasses import dataclass


@dataclass
class MCPServerConfig:
    name: str
    url: str
    authorization_token: str | None = None
    allowed_tools: list[str] | None = None


def build_openai_mcp_tool(config: MCPServerConfig) -> dict:
    tool: dict = {
        "type": "mcp",
        "server_label": config.name,
        "server_url": config.url,
        "require_approval": "always",
    }
    if config.allowed_tools:
        tool["allowed_tools"] = config.allowed_tools
    return tool


def build_anthropic_mcp_server(config: MCPServerConfig) -> dict:
    server = {"type": "url", "url": config.url, "name": config.name}
    if config.authorization_token:
        server["authorization_token"] = config.authorization_token
    return server
