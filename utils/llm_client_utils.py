
import os
from openai import OpenAI

def create_llm_client(provider="groq", api_key=None, model=None):
    """
    Creates an API client for either OpenAI or Groq.

    Args:
        provider (str): "openai" or "groq"
        api_key (str, optional): API key for the chosen provider.
        model (str, optional): Model name to store for convenience.

    Returns:
        dict: {"client": OpenAI instance, "model": model_name}
    """

    # Select defaults if not provided
    if provider == "groq":
        api_key = api_key or os.getenv("GROQ_API_KEY")
        base_url = "https://api.groq.com/openai/v1"
        default_model = "llama3-70b-8192"
    elif provider == "openai":
        api_key = api_key or os.getenv("OPENAI_API_KEY")
        base_url = "https://api.openai.com/v1"
        default_model = "gpt-4o"
    else:
        raise ValueError("Invalid provider. Use 'openai' or 'groq'.")

    # Create client
    client = OpenAI(api_key=api_key, base_url=base_url)

    return {
        "client": client,
        "model": model or default_model
    }
