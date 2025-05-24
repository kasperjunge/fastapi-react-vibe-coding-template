import uvicorn
from contextlib import asynccontextmanager
from backend.api import app
from backend.settings import settings
from backend.db import create_db_and_tables
from backend.db import run_migrations

def main() -> None:
    print("Hello from backend!!")

    reload = settings.ENVIRONMENT == "dev"

    uvicorn.run(
        "backend.main:app", 
        host=settings.BACKEND_HOST, 
        port=settings.BACKEND_PORT, 
        reload=reload
    )

if __name__ == "__main__":
    main()
