from typing import List

def suggest_rewrites(
    bullets: List[str],
    missing_keywords: List[str],
    max_suggestions: int = 5
) -> List[str]:
    """
    Suggests bullet rewrite guidance to improve ATS match.
    """

    suggestions = []

    for kw in missing_keywords[:max_suggestions]:
        suggestions.append(
            f"Consider incorporating keyword '{kw}' into a relevant bullet point."
        )

    return suggestions
