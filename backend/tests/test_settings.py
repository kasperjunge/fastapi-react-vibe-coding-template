import os

from dotenv import load_dotenv

from backend.settings import settings

load_dotenv()

def test_settings():
    assert settings.ENVIRONMENT == os.environ["ENVIRONMENT"]
    if settings.DATABASE_TYPE == "postgresql":
        assert settings.DATABASE_URL ==  "postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}".format(
            POSTGRES_USER=os.environ["POSTGRES_USER"],
            POSTGRES_PASSWORD=os.environ["POSTGRES_PASSWORD"],
                POSTGRES_HOST=os.environ["POSTGRES_HOST"],
                POSTGRES_PORT=os.environ["POSTGRES_PORT"],
                POSTGRES_DB=os.environ["POSTGRES_DB"]
            )
    else:
        assert settings.DATABASE_URL ==  "sqlite+aiosqlite:///{SQLITE_DB_PATH}".format(
            SQLITE_DB_PATH=settings.SQLITE_DB_PATH
        )