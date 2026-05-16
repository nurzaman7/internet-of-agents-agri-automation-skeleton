from __future__ import annotations

from typing import Any


class WeatherConnector:
    async def forecast(self, lat: float, lon: float, start_iso: str, end_iso: str) -> dict[str, Any]:
        # Replace with your national weather service, private weather API, or on-farm station fusion.
        return {
            "lat": lat,
            "lon": lon,
            "start": start_iso,
            "end": end_iso,
            "wind_speed_mps": 2.5,
            "precipitation_mm_hr": 0.0,
            "source": "simulated",
        }
