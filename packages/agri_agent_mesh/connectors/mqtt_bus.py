from __future__ import annotations

import json
from typing import Callable, Any

import paho.mqtt.client as mqtt

from agri_agent_mesh.config import Settings


class MQTTBus:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self.client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        if settings.mqtt_username:
            self.client.username_pw_set(settings.mqtt_username, settings.mqtt_password)

    def connect(self) -> None:
        self.client.connect(self.settings.mqtt_host, self.settings.mqtt_port, keepalive=60)

    def publish_json(self, topic: str, payload: dict[str, Any], qos: int = 1) -> None:
        self.client.publish(topic, json.dumps(payload), qos=qos)

    def subscribe_json(self, topic: str, handler: Callable[[str, dict[str, Any]], None]) -> None:
        def on_message(client, userdata, msg):
            try:
                data = json.loads(msg.payload.decode("utf-8"))
            except json.JSONDecodeError:
                data = {"raw": msg.payload.decode("utf-8", errors="replace")}
            handler(msg.topic, data)

        self.client.on_message = on_message
        self.client.subscribe(topic)
        self.client.loop_forever()
