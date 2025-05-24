from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


class UserRead(BaseModel):
    """Schema for reading users."""

    id: int
    email: EmailStr
    is_active: bool
    is_verified: bool
    created_at: datetime


class UserCreate(BaseModel):
    """Schema for creating users."""

    email: EmailStr
    password: str


class UserLogin(BaseModel):
    """Schema for logging in."""

    email: EmailStr
    password: str


class Token(BaseModel):
    """Returned JWT access token."""

    access_token: str
    token_type: str = "bearer"
