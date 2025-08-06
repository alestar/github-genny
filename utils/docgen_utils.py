# docgen.py

import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")  # Set your API key as an environment variable

def generate_doc(code: str, model="gpt-4") -> str:
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
        response = openai.ChatCompletion.create(
                    model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant that writes technical documentation."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.4,
            max_tokens=1024,
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"❌ Error: {e}"
