import pathlib
from typing import Literal
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

try:
    env_path = pathlib.Path(__file__).absolute().parents[3] / ".env"
    load_dotenv(dotenv_path=env_path)
    backend_root = pathlib.Path(__file__).absolute().parents[2]
except (IndexError, FileNotFoundError):
    pass

class Settings(BaseSettings):
    # Environment (dev, prod)
    ENVIRONMENT: str

    # Database Configuration
    DATABASE_TYPE: Literal["sqlite", "postgresql"] = "sqlite"
    
    # SQLite Configuration (default for development)
    SQLITE_DB_PATH: str = str(backend_root / "app.db")
    
    # PostgreSQL Configuration (for production or when DATABASE_TYPE=postgresql)
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: str = "5432"
    POSTGRES_DB: str = "db"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "secret"

    # Backend
    BACKEND_HOST: str
    BACKEND_PORT: int

    # Frontend
    FRONTEND_HOST: str
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

    # Email Configuration
    MAIL_USERNAME: str = ""
    MAIL_PASSWORD: str = ""
    MAIL_FROM: str = ""
    MAIL_PORT: int = 587
    MAIL_SERVER: str = "localhost"
    MAIL_FROM_NAME: str = "FastAPI App"
    MAIL_STARTTLS: bool = True
    MAIL_SSL_TLS: bool = False
    USE_CREDENTIALS: bool = True
    VALIDATE_CERTS: bool = True
    
    # Email Provider (mailhog, gmail, resend)
    EMAIL_PROVIDER: str = "mailhog"
    
    # Resend API (for production)
    RESEND_API_KEY: str = ""
    
    # Verification settings
    VERIFICATION_TOKEN_EXPIRE_HOURS: int = 24

    # For pydantic v2, use SettingsConfigDict instead of Config class
    model_config = SettingsConfigDict(
        env_prefix="",
        extra="ignore",
    )

    @property
    def FRONTEND_URL(self) -> str:
        return f"http://{self.FRONTEND_HOST}:{self.FRONTEND_PORT}"


    @property
    def DATABASE_URL(self) -> str:
        """Generate async database URL based on database type."""
        if self.DATABASE_TYPE.lower() == "sqlite":
            # Ensure directory exists for SQLite database
            db_path = pathlib.Path(self.SQLITE_DB_PATH)
            db_path.parent.mkdir(parents=True, exist_ok=True)
            return f"sqlite+aiosqlite:///{self.SQLITE_DB_PATH}"
        elif self.DATABASE_TYPE.lower() == "postgresql":
            return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        else:
            raise ValueError(f"Unsupported database type: {self.DATABASE_TYPE}")

    @property
    def DATABASE_URL_SYNC(self) -> str:
        """Generate sync database URL based on database type (for Alembic migrations)."""
        if self.DATABASE_TYPE.lower() == "sqlite":
            # Ensure directory exists for SQLite database
            db_path = pathlib.Path(self.SQLITE_DB_PATH)
            db_path.parent.mkdir(parents=True, exist_ok=True)
            return f"sqlite:///{self.SQLITE_DB_PATH}"
        elif self.DATABASE_TYPE.lower() == "postgresql":
            return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        else:
            raise ValueError(f"Unsupported database type: {self.DATABASE_TYPE}")


settings = Settings()

