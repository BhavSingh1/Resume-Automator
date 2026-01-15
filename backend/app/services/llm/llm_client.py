import os
import openai
from ...config import settings

# initialize OpenAI API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") or getattr(settings, "OPENAI_API_KEY", None)
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found in environment or settings")

openai.api_key = OPENAI_API_KEY

async def generate_text(prompt: str, model: str = "gpt-4", max_tokens: int = 500, temperature: float = 0.3) -> str:
    """
    Calls the OpenAI LLM asynchronously (via asyncio.to_thread).
    Returns the text output from the model.
    """
    import asyncio

    def sync_call():
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant for resume and cover letter generation."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=max_tokens,
            temperature=temperature
        )
        return response.choices[0].message.content.strip()

    # run blocking call in thread
    text = await asyncio.to_thread(sync_call)
    return text
