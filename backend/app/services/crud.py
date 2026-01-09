from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from ..models import db_models
from ..models import schemas
from ..utils import security

# User CRUD
async def get_user_by_email(db: AsyncSession, email: str):
    q = select(db_models.User).where(db_models.User.email == email)
    result = await db.execute(q)
    return result.scalars().first()

async def create_user(db: AsyncSession, user_in: schemas.UserCreate):
    hashed = security.hash_password(user_in.password)
    db_obj = db_models.User(email=user_in.email, full_name=user_in.full_name, hashed_password=hashed)
    db.add(db_obj)
    await db.commit()
    await db.refresh(db_obj)
    return db_obj

# MasterProfile CRUD
async def create_profile(db: AsyncSession, user_id: int, profile_in: schemas.MasterProfileCreate):
    db_obj = db_models.MasterProfile(user_id=user_id, title=profile_in.title, summary=profile_in.summary, data=profile_in.data)
    db.add(db_obj)
    await db.commit()
    await db.refresh(db_obj)
    return db_obj

async def get_profiles_for_user(db: AsyncSession, user_id: int):
    q = select(db_models.MasterProfile).where(db_models.MasterProfile.user_id == user_id)
    result = await db.execute(q)
    return result.scalars().all()

# Snippets
async def add_snippet(db: AsyncSession, profile_id: int, snippet_in: dict):
    db_obj = db_models.ResumeSnippet(profile_id=profile_id, section=snippet_in["section"], text=snippet_in["text"], tags=snippet_in.get("tags"))
    db.add(db_obj)
    await db.commit()
    await db.refresh(db_obj)
    return db_obj

