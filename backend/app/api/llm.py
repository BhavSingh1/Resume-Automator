from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from ..db import get_db
from ..models import db_models
from ..services.llm import resume_generator

router = APIRouter(prefix="/api/llm", tags=["llm"])

@router.post("/generate/{profile_id}")
async def generate_resume_and_cover(profile_id: int, job_description: str, db: AsyncSession = Depends(get_db)):
    # Fetch profile
    q = select(db_models.MasterProfile).where(db_models.MasterProfile.id == profile_id)
    res = await db.execute(q)
    profile = res.scalars().first()
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")

    # Generate resume bullets
    bullets = await resume_generator.generate_tailored_resume(profile.data, job_description)
    # Generate cover letter
    cover_letter = await resume_generator.generate_cover_letter(profile.data, job_description)

    return {
        "resume_bullets": bullets,
        "cover_letter": cover_letter
    }
