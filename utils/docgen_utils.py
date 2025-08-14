# docgen.py
from xml.etree.ElementTree import tostring

from utils.llm_client_utils import create_llm_client

llm_instance = create_llm_client(provider="groq", model="llama3-8b-8192")


def generate_doc_using_llm_client(code: str) -> str:
    """
    Generate documentation for a given block of code using ChatGPT.
    Returns a markdown-formatted summary.
    """
    if not code.strip():
        return "⚠️ Empty or unreadable code file."

    prompt = f"""
        You are an expert software documentation writer.
        
        Your task is to generate clear, concise documentation for the following code file.
        
        Explain:
        - The overall purpose of the file
        - Key classes and functions
        - Any important logic or design patterns
        
        Keep the response in markdown format with headers and bullet points.
        
        CODE:
        ```python
        {code[:3500]}  # Truncate if too long (adjustable)
        """

    try:
        response = llm_instance["client"].chat.completions.create(model=llm_instance["model"],
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant that writes technical documentation."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.4,
                    max_tokens=1024)
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ Error: {e}"

