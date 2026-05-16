from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    project_name: str = "AgriAgentMesh"
    environment: str = "local"
    log_level: str = "INFO"

    llm_provider: str = "openai"
    openai_api_key: str | None = None
    openai_model: str = "gpt-5.5"
    anthropic_api_key: str | None = None
    anthropic_model: str = "claude-sonnet-4-5"
    local_model_url: str = "http://localhost:11434/v1/chat/completions"
    local_model_name: str = "local-agent-model"

    mqtt_host: str = "localhost"
    mqtt_port: int = 1883
    mqtt_username: str | None = None
    mqtt_password: str | None = None
    mqtt_tls: bool = False

    database_url: str = "sqlite:///./agri_agent_mesh.db"
    redis_url: str = "redis://localhost:6379/0"
    require_human_approval_for_actuation: bool = True

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")


@lru_cache
def get_settings() -> Settings:
    return Settings()
