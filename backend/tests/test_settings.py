import os
from dotenv import load_dotenv

load_dotenv()

from backend.settings import settings

def test_settings():
    assert settings.ENVIRONMENT == os.environ["ENVIRONMENT"]
    assert settings.DATABASE_URL ==  "postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}".format(
        POSTGRES_USER=os.environ["POSTGRES_USER"],
        POSTGRES_PASSWORD=os.environ["POSTGRES_PASSWORD"],
        POSTGRES_HOST=os.environ["POSTGRES_HOST"],
        POSTGRES_PORT=os.environ["POSTGRES_PORT"],
        POSTGRES_DB=os.environ["POSTGRES_DB"]
    )