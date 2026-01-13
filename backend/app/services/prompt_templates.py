def resume_bullets_prompt(profile_json: dict, job_description: str) -> str:
    """
    Generates a prompt to create tailored resume bullets.
    profile_json: structured MasterProfile JSON
    job_description: full text of the job description
    """
    prompt = f"""
You are a resume expert.

Given the following candidate profile in JSON format:
{profile_json}

And the following job description:
{job_description}

Generate 5-7 concise, impact-oriented, tailored resume bullet points highlighting the most relevant skills, projects, and experience.
- Use professional action verbs.
- Emphasize achievements over duties.
- Keep each bullet under 35 words.
- Output as a JSON list of strings only.
"""
    return prompt

def cover_letter_prompt(profile_json: dict, job_description: str) -> str:
    """
    Generates a prompt to create a concise, one-page cover letter.
    """
    prompt = f"""
You are a professional career advisor.

Candidate profile (JSON):
{profile_json}

Job description:
{job_description}

Generate a concise, one-page cover letter tailored to this job:
- Use a professional, enthusiastic tone.
- Highlight relevant experience and skills.
- Include 2-3 sentences connecting candidate experience to the job.
- Output only plain text.
"""
    return prompt
