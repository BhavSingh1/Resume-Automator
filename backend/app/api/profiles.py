from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from ..models import schemas, db_models
from ..db import get_db
from ..services import crud

router = APIRouter(prefix="/api/profiles", tags=["profiles"])

@router.post("/user/{user_id}", response_model=schemas.MasterProfileRead, status_code=status.HTTP_201_CREATED)
async def create_profile_for_user(user_id: int, profile_in: schemas.MasterProfileCreate, db: AsyncSession = Depends(get_db)):
    # Ensure user exists
    q = select(db_models.User).where(db_models.User.id == user_id)
    res = await db.execute(q)
    user = res.scalars().first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    profile = await crud.create_profile(db, user_id, profile_in)
    return profile

@router.get("/user/{user_id}", response_model=list[schemas.MasterProfileRead])
async def list_profiles(user_id: int, db: AsyncSession = Depends(get_db)):
    profiles = await crud.get_profiles_for_user(db, user_id)
    return profiles
