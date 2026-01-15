from typing import List, Dict

def score_resume(
    resume_text: str,
    keywords: List[str]
) -> Dict[str, float]:
    """
    Scores resume against ATS keywords.
    Returns score + breakdown.
    """

    resume_text = resume_text.lower()

    matched = []
    missing = []

    for kw in keywords:
        if kw in resume_text:
            matched.append(kw)
        else:
            missing.append(kw)

    total = len(keywords)
    score = round((len(matched) / total) * 100, 2) if total else 0.0

    return {
        "score": score,
        "matched_keywords": matched,
        "missing_keywords": missing
    }
