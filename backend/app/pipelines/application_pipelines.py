from services.llm.resume_generator import generate_tailored_resume
from services.latex.latex_renderer import render_latex_to_pdf


class PipelineError(Exception):
    """Base pipeline exception."""


def run_application_pipeline():
    try:
        job = ()
        resume_text = generate_tailored_resume(
            profile=job.profile,
            job_description=job.description,
        )

        pdf_path = render_latex_to_pdf(resume_text)

        print(f"📄 Resume generated at: {pdf_path}")

    except Exception as e:
        raise PipelineError("Application pipeline failed") from e
