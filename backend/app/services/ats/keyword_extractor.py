import re
from collections import Counter
from typing import List

STOPWORDS = {
    "and", "or", "with", "to", "for", "of", "the", "a", "an",
    "in", "on", "by", "is", "are", "as", "at", "from"
}

def extract_keywords(job_description: str) -> List[str]:
    """
    Extracts ATS-relevant keywords from a job description.
    Rule-based baseline (fast, deterministic).
    """

    #Normalize text
    text = job_description.lower()

    #Remove punctuation
    text = re.sub(r"[^a-z0-9\s\+\#]", " ", text)

    #Tokenize
    tokens = text.split()

    #Filter stopwords & short tokens
    keywords = [
        t for t in tokens
        if t not in STOPWORDS and len(t) > 2
    ]

    #Frequency-based importance
    counts = Counter(keywords)

    #Return sorted keywords (most important first)
    return [kw for kw, _ in counts.most_common()]
