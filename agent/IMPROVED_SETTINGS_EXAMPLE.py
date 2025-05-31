"""
Improved Settings Configuration with Enhanced Validation and Security
This is an example of how the settings.py file could be improved.
"""

import pathlib
from typing import Literal, List
from pydantic import field_validator, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

try:
    env_path = pathlib.Path(__file__).absolute().parents[3] / ".env"
    load_dotenv(dotenv_path=env_path)
    backend_root = pathlib.Path(__file__).absolute().parents[2]
except (IndexError, FileNotFoundError):
    pass

class Settings(BaseSettings):
    # Environment (dev, prod, testing)
    ENVIRONMENT: Literal["dev", "prod", "testing"] = "dev"

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
    
    # Frontend API URL (CRITICAL - was missing in original)
    VITE_API_URL: str = "http://localhost:8000"
    
    # Admin user configuration
    ADMIN_EMAIL: str
    ADMIN_USERNAME: str
    ADMIN_PASSWORD: str
    ADMIN_FIRST_NAME: str
    ADMIN_LAST_NAME: str

    # Security Configuration
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    
    # CORS Configuration
    ALLOWED_ORIGINS: str = "http://localhost:5173,http://localhost:3000"
    
    # Rate Limiting
    RATE_LIMIT_REQUESTS: int = 100
    RATE_LIMIT_WINDOW: int = 60  # seconds
    
    # Logging Configuration
    LOG_LEVEL: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = "INFO"
    DEBUG_MODE: bool = False
    
    # Security Headers
    ENABLE_SECURITY_HEADERS: bool = True
    
    # API Documentation
    ENABLE_DOCS: bool = True
    ENABLE_REDOC: bool = True

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
    EMAIL_PROVIDER: Literal["mailhog", "gmail", "resend", "smtp"] = "mailhog"
    
    # Resend API (for production)
    RESEND_API_KEY: str = ""
    
    # Verification settings
    VERIFICATION_TOKEN_EXPIRE_HOURS: int = 24

    # Pydantic v2 configuration
    model_config = SettingsConfigDict(
        env_prefix="",
        extra="ignore",
        case_sensitive=True,
    )

    # Validation Methods
    @field_validator('SECRET_KEY')
    @classmethod
    def validate_secret_key(cls, v: str) -> str:
        """Validate SECRET_KEY strength and security."""
        if len(v) < 32:
            raise ValueError('SECRET_KEY must be at least 32 characters long for security')
        
        # Check for common weak values
        weak_keys = ['blabla', 'secret', 'change-me', 'your-secret-key', 'test-key']
        if v.lower() in weak_keys:
            raise ValueError(f'SECRET_KEY must not use weak/default values: {weak_keys}')
        
        return v

    @field_validator('ADMIN_PASSWORD')
    @classmethod
    def validate_admin_password(cls, v: str) -> str:
        """Validate admin password strength."""
        if len(v) < 8:
            raise ValueError('ADMIN_PASSWORD must be at least 8 characters long')
        
        # Check for common weak passwords
        weak_passwords = ['password', '123456', '1234567890', 'admin', 'admin123']
        if v.lower() in weak_passwords:
            raise ValueError(f'ADMIN_PASSWORD must not use common weak passwords: {weak_passwords}')
        
        return v

    @field_validator('ADMIN_EMAIL')
    @classmethod
    def validate_admin_email(cls, v: str) -> str:
        """Validate admin email format."""
        if '@' not in v or '.' not in v.split('@')[1]:
            raise ValueError('ADMIN_EMAIL must be a valid email address')
        return v

    @field_validator('POSTGRES_PORT')
    @classmethod
    def validate_postgres_port(cls, v: str) -> str:
        """Validate PostgreSQL port is numeric."""
        try:
            port = int(v)
            if not (1 <= port <= 65535):
                raise ValueError('POSTGRES_PORT must be between 1 and 65535')
        except ValueError:
            raise ValueError('POSTGRES_PORT must be a valid port number')
        return v

    @field_validator('BACKEND_PORT')
    @classmethod
    def validate_backend_port(cls, v: int) -> int:
        """Validate backend port range."""
        if not (1 <= v <= 65535):
            raise ValueError('BACKEND_PORT must be between 1 and 65535')
        return v

    @field_validator('ALLOWED_ORIGINS')
    @classmethod
    def validate_allowed_origins(cls, v: str) -> str:
        """Validate CORS origins format."""
        if v:
            origins = [origin.strip() for origin in v.split(',')]
            for origin in origins:
                if not origin.startswith(('http://', 'https://')):
                    raise ValueError(f'Invalid origin format: {origin}. Must start with http:// or https://')
        return v

    # Computed Properties
    @computed_field
    @property
    def FRONTEND_URL(self) -> str:
        """Generate frontend URL for email links and redirects."""
        protocol = "https" if self.ENVIRONMENT == "prod" else "http"
        return f"{protocol}://{self.FRONTEND_HOST}:{self.FRONTEND_PORT}"

    @computed_field
    @property
    def BACKEND_URL(self) -> str:
        """Generate backend URL."""
        protocol = "https" if self.ENVIRONMENT == "prod" else "http"
        return f"{protocol}://{self.BACKEND_HOST}:{self.BACKEND_PORT}"

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

    @computed_field
    @property
    def ALLOWED_ORIGINS_LIST(self) -> List[str]:
        """Convert ALLOWED_ORIGINS string to list for FastAPI CORS."""
        if not self.ALLOWED_ORIGINS:
            return ["*"] if self.ENVIRONMENT == "dev" else []
        return [origin.strip() for origin in self.ALLOWED_ORIGINS.split(',')]

    @computed_field
    @property
    def IS_DEVELOPMENT(self) -> bool:
        """Check if running in development mode."""
        return self.ENVIRONMENT == "dev"

    @computed_field
    @property
    def IS_PRODUCTION(self) -> bool:
        """Check if running in production mode."""
        return self.ENVIRONMENT == "prod"

    @computed_field
    @property
    def IS_TESTING(self) -> bool:
        """Check if running in testing mode."""
        return self.ENVIRONMENT == "testing"

    def get_email_config(self) -> dict:
        """Get email configuration based on provider."""
        base_config = {
            "MAIL_FROM": self.MAIL_FROM or f"noreply@{self.BACKEND_HOST}",
            "MAIL_FROM_NAME": self.MAIL_FROM_NAME,
        }
        
        if self.EMAIL_PROVIDER == "mailhog":
            return {
                **base_config,
                "MAIL_USERNAME": "",
                "MAIL_PASSWORD": "",
                "MAIL_PORT": 1025,
                "MAIL_SERVER": "localhost",
                "MAIL_STARTTLS": False,
                "MAIL_SSL_TLS": False,
                "USE_CREDENTIALS": False,
                "VALIDATE_CERTS": False,
            }
        elif self.EMAIL_PROVIDER == "gmail":
            return {
                **base_config,
                "MAIL_USERNAME": self.MAIL_USERNAME,
                "MAIL_PASSWORD": self.MAIL_PASSWORD,
                "MAIL_PORT": 587,
                "MAIL_SERVER": "smtp.gmail.com",
                "MAIL_STARTTLS": True,
                "MAIL_SSL_TLS": False,
                "USE_CREDENTIALS": True,
                "VALIDATE_CERTS": True,
            }
        else:  # Custom SMTP or Resend
            return {
                **base_config,
                "MAIL_USERNAME": self.MAIL_USERNAME,
                "MAIL_PASSWORD": self.MAIL_PASSWORD,
                "MAIL_PORT": self.MAIL_PORT,
                "MAIL_SERVER": self.MAIL_SERVER,
                "MAIL_STARTTLS": self.MAIL_STARTTLS,
                "MAIL_SSL_TLS": self.MAIL_SSL_TLS,
                "USE_CREDENTIALS": self.USE_CREDENTIALS,
                "VALIDATE_CERTS": self.VALIDATE_CERTS,
            }

    def get_cors_config(self) -> dict:
        """Get CORS configuration for FastAPI."""
        if self.IS_DEVELOPMENT:
            return {
                "allow_origins": self.ALLOWED_ORIGINS_LIST,
                "allow_credentials": True,
                "allow_methods": ["*"],
                "allow_headers": ["*"],
            }
        else:
            return {
                "allow_origins": self.ALLOWED_ORIGINS_LIST,
                "allow_credentials": True,
                "allow_methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
                "allow_headers": ["Authorization", "Content-Type"],
            }

    def get_security_headers(self) -> dict:
        """Get security headers configuration."""
        if not self.ENABLE_SECURITY_HEADERS:
            return {}
        
        return {
            "X-Content-Type-Options": "nosniff",
            "X-Frame-Options": "DENY",
            "X-XSS-Protection": "1; mode=block",
            "Strict-Transport-Security": "max-age=31536000; includeSubDomains" if self.IS_PRODUCTION else None,
            "Content-Security-Policy": "default-src 'self'" if self.IS_PRODUCTION else None,
        }

# Create settings instance
settings = Settings()

# Validation on startup
def validate_settings():
    """Validate critical settings on startup."""
    errors = []
    
    # Check required fields for production
    if settings.IS_PRODUCTION:
        if settings.SECRET_KEY in ['blabla', 'secret', 'change-me']:
            errors.append("Production SECRET_KEY must be changed from default value")
        
        if settings.DATABASE_TYPE == "sqlite":
            errors.append("Production should use PostgreSQL, not SQLite")
        
        if settings.EMAIL_PROVIDER == "mailhog":
            errors.append("Production should not use MailHog for email")
    
    # Check database connectivity requirements
    if settings.DATABASE_TYPE == "postgresql":
        required_pg_fields = [
            settings.POSTGRES_HOST,
            settings.POSTGRES_DB,
            settings.POSTGRES_USER,
            settings.POSTGRES_PASSWORD
        ]
        if not all(required_pg_fields):
            errors.append("PostgreSQL configuration incomplete")
    
    if errors:
        raise ValueError(f"Settings validation failed: {'; '.join(errors)}")

# Run validation
try:
    validate_settings()
except ValueError as e:
    print(f"⚠️  Settings Warning: {e}")
    if settings.IS_PRODUCTION:
        raise  # Fail hard in production 