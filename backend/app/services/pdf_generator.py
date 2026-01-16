from .latex.latex_renderer import render_latex
from .latex.latex_utils import bullets_to_latex, escape_latex
from datetime import date

def generate_resume_pdf(profile, resume_bullets, project_bullets):
    replacements = {
        "NAME": escape_latex(profile["name"]),
        "EMAIL": profile["email"],
        "PHONE": profile["phone"],
        "LOCATION": escape_latex(profile["location"]),
        "SUMMARY": escape_latex(profile["summary"]),
        "SKILLS": bullets_to_latex(profile["skills"]),
        "EXPERIENCE_BULLETS": bullets_to_latex(resume_bullets),
        "PROJECT_BULLETS": bullets_to_latex(project_bullets),
        "EDUCATION": escape_latex(profile["education"])
    }

    return render_latex("resume.tex", replacements, "resume")

def generate_cover_letter_pdf(profile: dict, cover_letter_text: str):
    """
    Generates a tailored cover letter PDF using LaTeX.
    """
    replacements = {
        "DATE": date.today().strftime("%B %d, %Y"),
        "COVER_LETTER_BODY": escape_latex(cover_letter_text),
        "NAME": escape_latex(profile["name"]),
    }

    return render_latex(
        template_name="cover_letter.tex",
        replacements=replacements,
        output_filename="cover_letter"
    )
    