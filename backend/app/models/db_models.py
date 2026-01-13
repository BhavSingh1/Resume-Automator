from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    ForeignKey,
    Text,
    JSON,
    func,
)
from sqlalchemy.orm import relationship
from ..db import Base
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy import Float


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(256), unique=True, index=True, nullable=False)
    full_name = Column(String(256), nullable=True)
    hashed_password = Column(String(512), nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    profiles = relationship("MasterProfile", back_populates="owner", cascade="all, delete-orphan")


class MasterProfile(Base):
    __tablename__ = "master_profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    title = Column(String(256), nullable=True)  # e.g., "Full Stack Engineer — Bhav"
    summary = Column(Text, nullable=True)
    data = Column(JSON, nullable=False)  # canonical structured JSON for profile (skills, projects, education)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), server_default=func.now())

    owner = relationship("User", back_populates="profiles")
    snippets = relationship("ResumeSnippet", back_populates="profile", cascade="all, delete-orphan")


# class ResumeSnippet(Base):
#     __tablename__ = "resume_snippets"

#     id = Column(Integer, primary_key=True, index=True)
#     profile_id = Column(Integer, ForeignKey("master_profiles.id", ondelete="CASCADE"), nullable=False)
#     section = Column(String(128), nullable=False)  # e.g., "experience", "projects", "skills"
#     text = Column(Text, nullable=False)
#     tags = Column(JSON, nullable=True)  # e.g., ["python","django","backend"]
#     embedding_id = Column(String(256), nullable=True)  # optional reference to vector DB object id
#     created_at = Column(DateTime(timezone=True), server_default=func.now())

#     profile = relationship("MasterProfile", back_populates="snippets")


class ResumeSnippet(Base):
    __tablename__ = "resume_snippets"

    id = Column(Integer, primary_key=True)
    profile_id = Column(Integer, ForeignKey("master_profiles.id"))
    section = Column(String)
    text = Column(Text)
    tags = Column(ARRAY(String), nullable=True)

    embedding = Column(ARRAY(Float), nullable=True)  # ← ADD THIS

    profile = relationship("MasterProfile", back_populates="snippets")

