from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from ..services.rag import snippetizer
from ..db import get_db
from ..services import crud
from ..models import db_models, schemas
from sqlalchemy import select

router = APIRouter(prefix="/api/snippets", tags=["snippets"])

@router.post("/profile/{profile_id}", response_model=list[schemas.ResumeSnippetRead])
async def create_snippets(profile_id: int, db: AsyncSession = Depends(get_db)):
    # fetch profile
    q = select(db_models.MasterProfile).where(db_models.MasterProfile.id == profile_id)
    result = await db.execute(q)
    profile = result.scalars().first()
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")

    # run snippetizer
    snippets = await snippetizer.snippetize_profile(db, profile)
    return snippets
