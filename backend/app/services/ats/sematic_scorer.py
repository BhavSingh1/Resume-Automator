import numpy as np
from typing import List, Dict
from app.services.rag.embedding_client import embed_text


def _cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b) + 1e-10))


async def semantic_match_score(
    resume_text: str,
    job_keywords: List[str]
) -> Dict[str, float]:
    """
    Computes semantic similarity between resume and job keywords.
    """

    if not job_keywords:
        return {
            "semantic_score": 0.0,
            "keyword_similarities": {}
        }

    #Embed resume once
    resume_embedding = np.array(
        await embed_text(resume_text),
        dtype="float32"
    )

    similarities = {}

    #Embed each keyword / requirement
    for kw in job_keywords:
        kw_embedding = np.array(
            await embed_text(kw),
            dtype="float32"
        )

        sim = _cosine_similarity(resume_embedding, kw_embedding)
        similarities[kw] = round(sim, 4)

    #Aggregate score
    semantic_score = round(
        sum(similarities.values()) / len(similarities),
        4
    )

    return {
        "semantic_score": semantic_score,
        "keyword_similarities": similarities
    }
