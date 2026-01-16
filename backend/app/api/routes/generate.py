from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Any

from backend.app.pipelines.application_pipelines import run_application_pipeline

router = APIRouter()

class GenerateRequest(BaseModel):
    profile: Dict[str, Any]
    job_description: str


class GenerateResponse(BaseModel):
    ats_score: float
    keywords_matched: list[str]
    bullets: list[str]
    latex: str
    pdf_url: str


@router.post("/generate", response_model=GenerateResponse)
async def generate_resume(payload: GenerateRequest):
    try:
        result = await run_application_pipeline(
            profile_json=payload.profile,
            job_description=payload.job_description
        )
        return result

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Resume generation failed: {str(e)}"
        )
