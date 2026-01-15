import faiss
import numpy as np
from typing import List

from .embedding_client import embed_text
from app.models.db_models import ResumeSnippet


def _normalize(vectors: np.ndarray) -> np.ndarray:
    """
    Normalize vectors for cosine similarity using inner product.
    """
    norms = np.linalg.norm(vectors, axis=1, keepdims=True)
    return vectors / np.clip(norms, 1e-10, None)


async def retrieve_top_snippets(
    job_description: str,
    snippets: List[ResumeSnippet],
    k: int = 8
) -> List[ResumeSnippet]:
    """
    Retrieves top-K relevant resume snippets using FAISS.
    """

    if not snippets:
        return []

    #Prepare texts
    snippet_texts = [s.text for s in snippets]

    #Generate embeddings
    snippet_embeddings = np.array(
        [await embed_text(text) for text in snippet_texts],
        dtype="float32"
    )

    job_embedding = np.array(
        [await embed_text(job_description)],
        dtype="float32"
    )

    #Normalize for cosine similarity
    snippet_embeddings = _normalize(snippet_embeddings)
    job_embedding = _normalize(job_embedding)

    #Create FAISS index (cosine via inner product)
    dim = snippet_embeddings.shape[1]
    index = faiss.IndexFlatIP(dim)

    #Add vectors
    index.add(snippet_embeddings)

    #Search
    scores, indices = index.search(job_embedding, k)

    #Map results back to snippets
    ranked_snippets = [snippets[i] for i in indices[0]]

    return ranked_snippets


# Optional future reranking:
# - Cross-encoder scoring
# - Section weighting (experience > projects)
# - ATS keyword boosting

