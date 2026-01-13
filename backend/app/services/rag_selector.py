from .embedding_client import embed_text
from .vector_store import VectorStore

async def select_relevant_snippets(snippets: list, job_description: str, k=6):
    dimension = len(snippets[0].embedding)
    store = VectorStore(dimension)

    for s in snippets:
        store.add(s.embedding, s.id)

    jd_embedding = await embed_text(job_description)
    best_ids = store.search(jd_embedding, k=k)

    return [s for s in snippets if s.id in best_ids]
