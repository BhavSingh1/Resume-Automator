from typing import List, Optional, Any
from pydantic import BaseModel, EmailStr
from datetime import datetime

# Shared / base
class UserBase(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None

class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    id: int
    is_active: bool
    is_superuser: bool
    created_at: Optional[datetime]

    class Config:
        orm_mode = True

class MasterProfileBase(BaseModel):
    title: Optional[str] = None
    summary: Optional[str] = None
    data: Any  # structured JSON

class MasterProfileCreate(MasterProfileBase):
    pass

class MasterProfileRead(MasterProfileBase):
    id: int
    user_id: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True

class ResumeSnippetBase(BaseModel):
    section: str
    text: str
    tags: Optional[List[str]] = None

class ResumeSnippetRead(ResumeSnippetBase):
    id: int
    profile_id: int
    created_at: Optional[datetime]

    class Config:
        orm_mode = True
