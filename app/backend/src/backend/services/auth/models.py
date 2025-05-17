from datetime import datetime
from typing import Optional, List
from enum import Enum
from sqlmodel import Field, SQLModel, Relationship
from sqlalchemy import UniqueConstraint

from backend.services.users.models import User


class TokenType(str, Enum):
    ACCESS = "access"
    REFRESH = "refresh"
    VERIFICATION = "verification"
    PASSWORD_RESET = "password_reset"


class AuthToken(SQLModel, table=True):
    """Token model for authentication."""
    __tablename__ = "auth_tokens"

    id: Optional[int] = Field(default=None, primary_key=True)
    token: str = Field(unique=True, index=True)
    token_type: TokenType
    expires_at: datetime
    created_at: datetime = Field(default_factory=datetime.utcnow)
    is_revoked: bool = Field(default=False)
    
    # Foreign keys
    user_id: Optional[int] = Field(default=None, foreign_key="users.id")
    
    # Relationships
    user: Optional[User] = Relationship(back_populates="auth_tokens")


class OAuthProvider(str, Enum):
    GOOGLE = "google"
    GITHUB = "github"

class OAuthAccount(SQLModel, table=True):
    """OAuth account model for external authentication providers."""
    __tablename__ = "oauth_accounts"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    provider: OAuthProvider
    provider_user_id: str
    access_token: str
    refresh_token: Optional[str] = None
    expires_at: Optional[datetime] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    
    # Foreign keys
    user_id: int = Field(foreign_key="users.id")
    
    # Relationships
    user: User = Relationship(back_populates="oauth_accounts")
    
    # Constraints
    __table_args__ = (
        UniqueConstraint("provider", "provider_user_id"),
    )
