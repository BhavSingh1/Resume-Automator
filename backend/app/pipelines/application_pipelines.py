from services.llm.resume_generator import generate_tailored_resume
from typing import Dict, Any

from services.rag.vector_search import retrieve_top_snippets as retrieve_relevant_snippets
from services.ats.sematic_scorer import semantic_match_score as score_against_job
from services.llm.resume_generator import (
    generate_tailored_resume,
    generate_cover_letter,
)
from services.latex.latex_renderer import render_latex as render_resume_to_pdf

class PipelineError(Exception):
    """Top-level pipeline failure."""
    pass


async def run_application_pipeline(
    *,
    profile_json: Dict[str, Any],
    job_description: str,
) -> Dict[str, Any]:
    """
    End-to-end orchestration pipeline.

    Steps:
    1. Retrieve top-K relevant snippets (RAG)
    2. Score ATS match
    3. Generate tailored resume bullets
    4. Generate LaTeX + PDF
    """

    try:
        # RAG: retrieve best snippets
        snippets = await retrieve_relevant_snippets(
            profile_json=profile_json,
            job_description=job_description,
            top_k=12,
        )

        # ATS scoring
        ats_result = score_against_job(
            snippets=snippets,
            job_description=job_description,
        )

        # Resume generation
        bullets = await generate_tailored_resume(
            profile_json=profile_json,
            job_description=job_description,
        )

        # Cover letter (optional, but useful)
        cover_letter = await generate_cover_letter(
            profile_json=profile_json,
            job_description=job_description,
        )

        # LaTeX → PDF
        latex_source, pdf_path = render_resume_to_pdf(
            bullets=bullets,
            cover_letter=cover_letter,
        )

        return {
            "ats_score": ats_result.score,
            "keywords_matched": ats_result.matched_keywords,
            "bullets": bullets,
            "latex": latex_source,
            "pdf_url": pdf_path,
        }

    except Exception as e:
        raise PipelineError("Application pipeline failed") from e

