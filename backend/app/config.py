from pydantic.v1 import BaseSettings, PostgresDsn, Field

class Settings(BaseSettings):
    DATABASE_URL: PostgresDsn = Field(..., env="DATABASE_URL")
    REDIS_URL: str | None = None
    APP_NAME: str = "resume-automator-backend"
    # Add more settings later like OPENAI_API_KEY etc.

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
