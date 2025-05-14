import uuid
from datetime import datetime
from enum import Enum
from typing import Optional

from sqlmodel import Field, Index, SQLModel


class UserRole(str, Enum):
    USER = "user"
    ADMIN = "admin"


class User(SQLModel, table=True):
    """User model representing application users in the database."""
    
    __table_args__ = (
        Index("ix_user_email", "email", unique=True),
    )
    
    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
        index=True,
    )
    email: str = Field(...)
    password_hash: str = Field(...)
    name: str = Field(...)
    is_active: bool = Field(default=True)
    is_verified: bool = Field(default=False)
    role: UserRole = Field(default=UserRole.USER)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    
    class Config:
        json_schema_extra = {
            "example": {
                "email": "user@example.com",
                "name": "John Doe",
                "is_active": True,
                "is_verified": False,
                "role": "user",
            }
        }
