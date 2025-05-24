from datetime import datetime
from typing import Optional, List
from enum import Enum
from sqlmodel import Field, SQLModel, Relationship
from fastapi_users.db import SQLModelBaseUserTable, SQLModelBaseOAuthAccountTable


class UserRole(str, Enum):
    USER = "user"
    ADMIN = "admin"


class UserStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    PENDING = "pending"


class OAuthAccount(SQLModel, SQLModelBaseOAuthAccountTable, table=True):
    pass


class User(SQLModel, SQLModelBaseUserTable, table=True):
    """User model for authentication and user management."""
    __tablename__ = "users"

    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(unique=True, index=True)
    username: str = Field(unique=True, index=True)
    hashed_password: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    bio: Optional[str] = None
    profile_image_url: Optional[str] = None
    role: UserRole = Field(default=UserRole.USER)
    status: UserStatus = Field(default=UserStatus.PENDING)
    is_email_verified: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    
    # Define relationships
    oauth_accounts: List[OAuthAccount] = Relationship(back_populates="user", sa_relationship_kwargs={"cascade": "all, delete-orphan"})

