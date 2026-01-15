from .llm_client import generate_text
from .prompt_templates import resume_bullets_prompt, cover_letter_prompt
import json


async def generate_tailored_resume(profile_json: dict, snippets: list, job_description: str) -> list[str]:
    """
    Generates tailored resume bullet points from profile and job description.
    Returns a list of strings (bullet points).
    """
    context = snippets_to_prompt(snippets)
    prompt = resume_bullets_prompt(context, job_description)
    text = await generate_text(prompt, max_tokens=400)
    # Try to parse JSON list
    try:
        bullets = json.loads(text)
        if isinstance(bullets, list):
            bullets = [str(b).strip() for b in bullets]
        else:
            bullets = [text.strip()]
    except json.JSONDecodeError:
        # fallback: treat entire output as one bullet
        bullets = [text.strip()]
    return bullets

async def generate_cover_letter(profile_json: dict, snippets: list, job_description: str) -> str:
    """
    Generates a concise, tailored cover letter from profile and job description.
    Returns string of plain text.
    """
    context = snippets_to_prompt(snippets)
    prompt = cover_letter_prompt(context, job_description)
    text = await generate_text(prompt, max_tokens=500)

    return text.strip()

def snippets_to_prompt(snippets: list) -> str:
    """
    Converts selected ResumeSnippet objects into prompt-friendly text.
    """
    lines = []
    for s in snippets:
        lines.append(f"[{s.section.upper()}] {s.text}")
    return "\n".join(lines)

