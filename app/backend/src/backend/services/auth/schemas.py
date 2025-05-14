from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field


class TokenData(BaseModel):
    """Data embedded in JWT token"""
    user_id: UUID
    role: str
    exp: datetime


class Token(BaseModel):
    """Token response schema"""
    access_token: str
    token_type: str = "bearer"
    refresh_token: str
    expires_at: datetime


class UserCreate(BaseModel):
    """User registration schema"""
    email: EmailStr
    password: str = Field(..., min_length=8)
    name: str


class UserLogin(BaseModel):
    """User login schema"""
    email: EmailStr
    password: str


class RefreshToken(BaseModel):
    """Schema for refresh token request"""
    refresh_token: str
