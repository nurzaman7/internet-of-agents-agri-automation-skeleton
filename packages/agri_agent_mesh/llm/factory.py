from agri_agent_mesh.config import get_settings
from agri_agent_mesh.llm.anthropic_adapter import AnthropicAdapter
from agri_agent_mesh.llm.base import LLMClient
from agri_agent_mesh.llm.local_adapter import LocalAdapter
from agri_agent_mesh.llm.openai_adapter import OpenAIAdapter


def make_llm_client() -> LLMClient:
    settings = get_settings()
    provider = settings.llm_provider.lower()
    if provider == "openai":
        return OpenAIAdapter(settings)
    if provider == "anthropic":
        return AnthropicAdapter(settings)
    if provider == "local":
        return LocalAdapter(settings)
    raise ValueError(f"Unsupported LLM provider: {settings.llm_provider}")
