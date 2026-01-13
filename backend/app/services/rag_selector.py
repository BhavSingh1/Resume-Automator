from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
import numpy as np
import faiss

from ..models import db_models
from .embedding_client import embed_text


async def select_relevant_snippets(
    db: AsyncSession,
    profile_id: int,
    job_description: str,
    k: int = 6
) -> list[db_models.ResumeSnippet]:
    """
    Selects the top-K most relevant resume snippets for a job description
    using vector similarity search (FAISS).
    """

    # Load snippets with embeddings
    result = await db.execute(
        select(db_models.ResumeSnippet)
        .where(db_models.ResumeSnippet.profile_id == profile_id)
        .where(db_models.ResumeSnippet.embedding.isnot(None))
    )

    snippets = result.scalars().all()

    if not snippets:
        return []

    # Prepare FAISS index
    embeddings = np.array(
        [s.embedding for s in snippets],
        dtype="float32"
    )

    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    # Embed job description
    jd_embedding = await embed_text(job_description)
    jd_vec = np.array([jd_embedding], dtype="float32")

    # Search
    _, indices = index.search(jd_vec, k)

    # Map results back to snippets
    selected_snippets = [snippets[i] for i in indices[0]]

    return selected_snippets
