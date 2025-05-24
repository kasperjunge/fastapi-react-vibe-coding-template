from __future__ import annotations

from typing import Optional
from uuid import uuid4

from sqlmodel import Session, select

from .models import User
from .utils import hash_password, verify_password, create_access_token


class AuthService:
    """Simple authentication service."""

    def create_user(self, session: Session, email: str, password: str) -> User:
        user = session.exec(select(User).where(User.email == email)).first()
        if user:
            raise ValueError("User already exists")
        new_user = User(
            email=email,
            hashed_password=hash_password(password),
            verification_token=str(uuid4()),
        )
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        return new_user

    def authenticate(self, session: Session, email: str, password: str) -> Optional[User]:
        user = session.exec(select(User).where(User.email == email)).first()
        if user and verify_password(password, user.hashed_password):
            return user
        return None

    def verify_email(self, session: Session, token: str) -> bool:
        user = session.exec(select(User).where(User.verification_token == token)).first()
        if not user:
            return False
        user.is_verified = True
        user.verification_token = None
        session.add(user)
        session.commit()
        return True

    def request_password_reset(self, session: Session, email: str) -> Optional[str]:
        user = session.exec(select(User).where(User.email == email)).first()
        if not user:
            return None
        user.reset_token = str(uuid4())
        session.add(user)
        session.commit()
        return user.reset_token

    def reset_password(self, session: Session, token: str, new_password: str) -> bool:
        user = session.exec(select(User).where(User.reset_token == token)).first()
        if not user:
            return False
        user.hashed_password = hash_password(new_password)
        user.reset_token = None
        session.add(user)
        session.commit()
        return True

    def create_token_for_user(self, user: User) -> str:
        return create_access_token({"sub": str(user.id)})
