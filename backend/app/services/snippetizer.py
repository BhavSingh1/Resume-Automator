from sqlalchemy.ext.asyncio import AsyncSession
from ..models import db_models

# Define default sections we expect in MasterProfile.data
DEFAULT_SECTIONS = ["summary", "skills", "projects", "experience", "education"]

async def snippetize_profile(db: AsyncSession, profile: db_models.MasterProfile) -> list[db_models.ResumeSnippet]:
    """
    Converts a MasterProfile JSON into ResumeSnippet rows.
    - db: AsyncSession
    - profile: MasterProfile instance
    Returns a list of created ResumeSnippet objects.
    """
    snippets_created = []

    data = profile.data  # canonical JSON
    # Iterate through expected sections
    for section in DEFAULT_SECTIONS:
        if section in data:
            content = data[section]
            # Handle different content types
            if isinstance(content, list):
                # create snippet per item
                for item in content:
                    text = ""
                    tags = []
                    if isinstance(item, dict):
                        text = item.get("description") or item.get("title") or str(item)
                        tags = item.get("tags") or []
                    else:
                        text = str(item)
                    snippet = db_models.ResumeSnippet(
                        profile_id=profile.id,
                        section=section,
                        text=text,
                        tags=tags if tags else None
                    )
                    db.add(snippet)
                    snippets_created.append(snippet)
            elif isinstance(content, str):
                snippet = db_models.ResumeSnippet(
                    profile_id=profile.id,
                    section=section,
                    text=content,
                    tags=None
                )
                db.add(snippet)
                snippets_created.append(snippet)
            else:
                # fallback, convert to string
                snippet = db_models.ResumeSnippet(
                    profile_id=profile.id,
                    section=section,
                    text=str(content),
                    tags=None
                )
                db.add(snippet)
                snippets_created.append(snippet)

    # commit all snippets
    await db.commit()

    # refresh objects
    for s in snippets_created:
        await db.refresh(s)

    return snippets_created
