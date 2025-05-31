import pathlib
from typing import Literal
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import computed_field
from dotenv import load_dotenv

try:
    env_path = pathlib.Path(__file__).absolute().parents[3] / ".env"
    load_dotenv(dotenv_path=env_path)
    backend_root = pathlib.Path(__file__).absolute().parents[2]
except (IndexError, FileNotFoundError):
    pass

class Settings(BaseSettings):
    # Environment (local, prod)
    ENVIRONMENT: Literal["local", "prod"] = "local"

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

    # Backend Configuration
    BACKEND_HOST: str = "localhost"
    BACKEND_PORT: int = 8000
    
    # Frontend Configuration
    FRONTEND_HOST: str = "localhost"
    FRONTEND_PORT: str = "5173"
    
    # Domain Configuration (for production)
    # When ENVIRONMENT=prod, these override the HOST:PORT pattern
    DOMAIN: str = ""  # e.g., "example.com" for production
    BACKEND_PATH: str = ""  # e.g., "/api" if backend is served under a path
    FRONTEND_PATH: str = ""  # e.g., "" for root or "/app" for subpath
    
    # SSL Configuration
    USE_SSL: bool = False  # Automatically true for production unless overridden
    
    # CORS Configuration
    ALLOWED_ORIGINS: str = ""  # Comma-separated list, auto-generated if empty

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

    @computed_field
    @property
    def IS_PRODUCTION(self) -> bool:
        """Check if running in production environment."""
        return self.ENVIRONMENT == "prod"

    @computed_field
    @property
    def IS_LOCAL(self) -> bool:
        """Check if running in local development environment."""
        return self.ENVIRONMENT == "local"

    @computed_field
    @property
    def PROTOCOL(self) -> str:
        """Get the appropriate protocol (http/https)."""
        if self.IS_PRODUCTION:
            return "https" if self.USE_SSL or self.DOMAIN else "http"
        return "http"

    @computed_field
    @property
    def BACKEND_URL(self) -> str:
        """Generate backend URL based on environment."""
        if self.IS_PRODUCTION and self.DOMAIN:
            # Production with custom domain
            base_url = f"{self.PROTOCOL}://{self.DOMAIN}"
            return f"{base_url}{self.BACKEND_PATH}" if self.BACKEND_PATH else base_url
        else:
            # Local development or production without custom domain
            return f"{self.PROTOCOL}://{self.BACKEND_HOST}:{self.BACKEND_PORT}"

    @computed_field
    @property
    def FRONTEND_URL(self) -> str:
        """Generate frontend URL based on environment."""
        if self.IS_PRODUCTION and self.DOMAIN:
            # Production with custom domain
            base_url = f"{self.PROTOCOL}://{self.DOMAIN}"
            return f"{base_url}{self.FRONTEND_PATH}" if self.FRONTEND_PATH else base_url
        else:
            # Local development or production without custom domain
            return f"{self.PROTOCOL}://{self.FRONTEND_HOST}:{self.FRONTEND_PORT}"

    @computed_field
    @property
    def API_URL(self) -> str:
        """Generate API URL for frontend consumption."""
        if self.IS_PRODUCTION and self.DOMAIN:
            # In production with same domain, API is relative or absolute path
            if self.BACKEND_PATH:
                return self.BACKEND_PATH  # Relative path like "/api"
            else:
                return ""  # Same domain, no path
        else:
            # Local development: full URL to backend
            return self.BACKEND_URL

    @computed_field
    @property
    def CORS_ORIGINS(self) -> list[str]:
        """Generate CORS origins list."""
        if self.ALLOWED_ORIGINS:
            return [origin.strip() for origin in self.ALLOWED_ORIGINS.split(",")]
        
        # Auto-generate based on environment
        origins = []
        
        if self.IS_LOCAL:
            # Local development: include common development URLs
            origins.extend([
                f"http://localhost:{self.FRONTEND_PORT}",
                f"http://127.0.0.1:{self.FRONTEND_PORT}",
                "http://localhost:3000",  # Common React dev port
                "http://127.0.0.1:3000",
            ])
        
        # Always include the configured frontend URL
        if self.FRONTEND_URL not in origins:
            origins.append(self.FRONTEND_URL)
            
        return origins

    @computed_field
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

    @computed_field
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

