import openai
import asyncio
from ...config import settings

openai.api_key = settings.OPENAI_API_KEY

async def embed_text(text: str, model="text-embedding-3-large") -> list[float]:
    def sync_call():
        return openai.Embedding.create(
            model=model,
            input=text
        )["data"][0]["embedding"]

    return await asyncio.to_thread(sync_call)
