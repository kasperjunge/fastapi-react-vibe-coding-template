import os
from sqlmodel import SQLModel, create_engine, Session

os.environ.setdefault("ENVIRONMENT", "test")
os.environ.setdefault("POSTGRES_HOST", "localhost")
os.environ.setdefault("POSTGRES_PORT", "5432")
os.environ.setdefault("POSTGRES_DB", "test")
os.environ.setdefault("POSTGRES_USER", "user")
os.environ.setdefault("POSTGRES_PASSWORD", "password")

from backend.services.auth.service import AuthService
from backend.services.auth.models import User

engine = create_engine("sqlite:///:memory:")
SQLModel.metadata.create_all(engine)
service = AuthService()


def test_register_and_login():
    with Session(engine) as session:
        user = service.create_user(session, "u@example.com", "pass")
        assert user.email == "u@example.com"
        auth = service.authenticate(session, "u@example.com", "pass")
        assert auth is not None
        token = service.create_token_for_user(user)
        assert token


def test_email_verification():
    with Session(engine) as session:
        user = service.create_user(session, "v@example.com", "pass")
        token = user.verification_token
        ok = service.verify_email(session, token)
        assert ok
        session.refresh(user)
        assert user.is_verified
