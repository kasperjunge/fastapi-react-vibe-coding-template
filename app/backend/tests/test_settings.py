import os
from dotenv import load_dotenv

load_dotenv()

from backend.settings import settings

def test_settings():
    assert settings.ENVIRONMENT == os.environ["ENVIRONMENT"]
    assert settings.DATABASE_URL ==  "postgresql://{PGUSER}:{PGPASSWORD}@{PGHOST}:{PGPORT}/{PGDATABASE}".format(
        PGUSER=os.environ["PGUSER"],
        PGPASSWORD=os.environ["PGPASSWORD"],
        PGHOST=os.environ["PGHOST"],
        PGPORT=os.environ["PGPORT"],
        PGDATABASE=os.environ["PGDATABASE"]
    )