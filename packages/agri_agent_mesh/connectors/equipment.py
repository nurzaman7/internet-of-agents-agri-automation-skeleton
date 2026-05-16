from __future__ import annotations

from typing import Any


class EquipmentConnector:
    """Base connector for UAVs, robots, vehicles, valves, pumps, and sprayers.

    Replace this with hardware-specific adapters such as MAVLink, ROS2, Modbus, OPC-UA,
    CAN bus, LoRaWAN network server APIs, or vendor REST APIs.
    """

    async def dispatch(self, device_id: str, action: str, params: dict[str, Any]) -> dict[str, Any]:
        return {
            "device_id": device_id,
            "action": action,
            "params": params,
            "status": "simulated",
        }
