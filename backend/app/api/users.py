from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from ..models import schemas, db_models
from ..db import get_db
from ..services import crud

router = APIRouter(prefix="/api/users", tags=["users"])

@router.post("/register", response_model=schemas.UserRead, status_code=status.HTTP_201_CREATED)
async def register_user(user_in: schemas.UserCreate, db: AsyncSession = Depends(get_db)):
    existing = await crud.get_user_by_email(db, user_in.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    user = await crud.create_user(db, user_in)
    return user

@router.get("/{user_id}", response_model=schemas.UserRead)
async def get_user(user_id: int, db: AsyncSession = Depends(get_db)):
    q = select(db_models.User).where(db_models.User.id == user_id)
    res = await db.execute(q)
    user = res.scalars().first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
