from typing import Dict


def hybrid_ats_score(
    keyword_score: float,
    semantic_score: float,
    keyword_weight: float = 0.6,
    semantic_weight: float = 0.4
) -> float:
    """
    Combines keyword and semantic ATS scores.
    """

    return round(
        (keyword_score * keyword_weight) +
        (semantic_score * 100 * semantic_weight),
        2
    )
