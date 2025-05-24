import pathlib
import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

try:
    env_path = pathlib.Path(__file__).absolute().parents[4] / ".env"
    load_dotenv(dotenv_path=env_path)
except (IndexError, FileNotFoundError):
    pass

class Settings(BaseSettings):
    # Environment (local, dev, prod)
    ENVIRONMENT: str

    # Postgres DB
    PGHOST: str
    PGPORT: str
    PGDATABASE: str
    PGUSER: str
    PGPASSWORD: str

    # Backend
    BACKEND_PORT: int
    BACKEND_HOST: str

    # Frontend
    FRONTEND_PORT: str
    VITE_API_URL: str
    
    # JWT Settings
    JWT_SECRET_KEY: str
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int
    JWT_REFRESH_TOKEN_EXPIRE_DAYS: int
    JWT_ALGORITHM: str

    # SuperTokens
    SUPERTOKENS_CONNECTION_URI: str
    SUPERTOKENS_API_KEY: str | None = None

    # Admin user
    ADMIN_EMAIL: str
    ADMIN_USERNAME: str
    ADMIN_PASSWORD: str
    ADMIN_FIRST_NAME: str
    ADMIN_LAST_NAME: str

    # For pydantic v2, use SettingsConfigDict instead of Config class
    model_config = SettingsConfigDict(
        env_prefix="",
        extra="ignore",
    )

    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql://{self.PGUSER}:{self.PGPASSWORD}@{self.PGHOST}:{self.PGPORT}/{self.PGDATABASE}"

settings = Settings()

