import pathlib
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

try:
    env_path = pathlib.Path(__file__).absolute().parents[3] / ".env"
    load_dotenv(dotenv_path=env_path)
except (IndexError, FileNotFoundError):
    pass

class Settings(BaseSettings):
    # Environment (dev, prod)
    ENVIRONMENT: str

    # Postgres DB
    POSTGRES_HOST: str
    POSTGRES_PORT: str
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    # Backend
    BACKEND_HOST: str
    BACKEND_PORT: int

    # Frontend
    VITE_API_URL: str
    FRONTEND_PORT: str
    
    # Admin user
    ADMIN_EMAIL: str
    ADMIN_USERNAME: str
    ADMIN_PASSWORD: str
    ADMIN_FIRST_NAME: str
    ADMIN_LAST_NAME: str

    # Auth
    SECRET_KEY: str
    # ALGORITHM: str
    # ACCESS_TOKEN_EXPIRE_MINUTES: int
    # REFRESH_TOKEN_EXPIRE_DAYS: int

    # For pydantic v2, use SettingsConfigDict instead of Config class
    model_config = SettingsConfigDict(
        env_prefix="",
        extra="ignore",
    )

    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    @property
    def DATABASE_URL_SYNC(self) -> str:
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"


settings = Settings()

