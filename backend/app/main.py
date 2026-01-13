from fastapi import FastAPI
from .config import settings
from .api import users, profiles
from .db import engine, Base
import asyncio
from .api import users, profiles, snippets

app = FastAPI(title="Resume Automator - Backend", version="0.1.0")

# include routers
app.include_router(users.router)
app.include_router(profiles.router)
app.include_router(snippets.router)


@app.get("/health")
def health():
    return {"status": "ok", "service": settings.APP_NAME}

# Optional: convenience endpoint to create tables (development only).
# Production: prefer alembic migrations instead.
@app.post("/dev/create-tables")
async def create_tables():
    # CAREFUL: This creates tables using metadata.create_all and should not replace migrations.
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    return {"status": "tables_created"}  

