"""MCP server placeholder.

Use this service to expose farm tools to compatible AI clients. Keep tools narrow,
read-only by default, and require approval for any mutation or physical action.
"""

from fastapi import FastAPI

app = FastAPI(title="AgriAgentMesh MCP Tool Facade", version="0.1.0")


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "service": "mcp-tool-facade"}


@app.get("/tools/farm_status")
def farm_status(farm_id: str) -> dict:
    return {
        "farm_id": farm_id,
        "status": "simulated",
        "message": "Replace this endpoint with an MCP server implementation or gateway.",
    }
