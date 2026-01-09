from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from .config import settings

DATABASE_URL = settings.DATABASE_URL

# Async engine
engine: AsyncEngine = create_async_engine(
    DATABASE_URL,
    future=True,
    echo=False,  # set True while debugging, prints  every SQL query
)

# Async session factory, expire_on_commit=False recommended for FastAPI usage
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False,
    autocommit=False,
)

Base = declarative_base()

# Dependency for FastAPI
async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session
