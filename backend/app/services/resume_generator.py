from .llm_client import generate_text
from .prompt_templates import resume_bullets_prompt, cover_letter_prompt
import json

async def generate_tailored_resume(profile_json: dict, job_description: str) -> list[str]:
    """
    Generates tailored resume bullet points from profile and job description.
    Returns a list of strings (bullet points).
    """
    prompt = resume_bullets_prompt(profile_json, job_description)
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

async def generate_cover_letter(profile_json: dict, job_description: str) -> str:
    """
    Generates a concise, tailored cover letter from profile and job description.
    Returns string of plain text.
    """
    prompt = cover_letter_prompt(profile_json, job_description)
    text = await generate_text(prompt, max_tokens=500)
    return text.strip()
