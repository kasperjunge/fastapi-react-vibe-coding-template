import os

# Minimal environment variables so settings can load
os.environ.setdefault("ENVIRONMENT", "test")
os.environ.setdefault("POSTGRES_HOST", "localhost")
os.environ.setdefault("POSTGRES_PORT", "5432")
os.environ.setdefault("POSTGRES_DB", "db")
os.environ.setdefault("POSTGRES_USER", "user")
os.environ.setdefault("POSTGRES_PASSWORD", "password")

from backend.settings import settings


def test_settings():
    assert settings.ENVIRONMENT == os.environ["ENVIRONMENT"]
    expected = "postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}".format(
        POSTGRES_USER=os.environ["POSTGRES_USER"],
        POSTGRES_PASSWORD=os.environ["POSTGRES_PASSWORD"],
        POSTGRES_HOST=os.environ["POSTGRES_HOST"],
        POSTGRES_PORT=os.environ["POSTGRES_PORT"],
        POSTGRES_DB=os.environ["POSTGRES_DB"],
    )
    assert settings.DATABASE_URL == expected
