"""LLM Configuration module"""

import os
from crewai.llm import LLM


def get_llm():
    """Initialize and return the LLM based on provider choice"""
    provider = os.getenv("LLM_PROVIDER", "openai").lower()

    if provider == "azure":
        # Azure OpenAI configuration
        deployment = os.getenv('AZURE_OPENAI_DEPLOYMENT', 'gpt-4')

        # Get Azure credentials
        api_key = os.getenv("AZURE_OPENAI_API_KEY") or os.getenv("AZURE_API_KEY", "")
        api_base = os.getenv("AZURE_OPENAI_ENDPOINT") or os.getenv("AZURE_API_BASE", "")
        api_version = os.getenv("AZURE_OPENAI_API_VERSION") or os.getenv("AZURE_API_VERSION", "2024-02-15-preview")

        # Set environment variables that LiteLLM expects for Azure OpenAI
        os.environ["AZURE_API_KEY"] = api_key
        os.environ["AZURE_API_BASE"] = api_base
        os.environ["AZURE_API_VERSION"] = api_version

        # Use azure/ prefix and let LiteLLM use env vars automatically
        return LLM(model=f"azure/{deployment}")
    else:
        # Regular OpenAI configuration
        return LLM(
            model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
            api_key=os.getenv("OPENAI_API_KEY")
        )


def validate_config():
    """
    Validate LLM configuration based on provider

    Returns:
        tuple: (is_valid: bool, error_message: str)
    """
    provider = os.getenv("LLM_PROVIDER", "openai").lower()

    if provider == "openai":
        if not os.getenv("OPENAI_API_KEY"):
            return False, "Please configure your OpenAI API Key in the sidebar!"
    else:  # azure
        required_fields = [
            os.getenv("AZURE_OPENAI_API_KEY"),
            os.getenv("AZURE_OPENAI_ENDPOINT"),
            os.getenv("AZURE_OPENAI_DEPLOYMENT")
        ]
        if not all(required_fields):
            return False, "Please configure all Azure OpenAI fields in the sidebar!"

    return True, ""
