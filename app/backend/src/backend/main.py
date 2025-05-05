import uvicorn
from contextlib import asynccontextmanager
from backend.api import app
from backend.settings import settings
from backend.database import create_db_and_tables
from backend.database import run_migrations

@asynccontextmanager
async def lifespan(app):
    # Run on startup
    # First run migrations to ensure schema is up to date
    try:
        run_migrations()
    except Exception as e:
        print(f"Warning: Failed to run migrations: {e}")
    
    # Then create any tables that might be missing
    create_db_and_tables()
    
    yield
    # Run on shutdown (if needed)

def main() -> None:
    print("Hello from backend!!")

    reload = settings.ENVIRONMENT == "dev"

    uvicorn.run(
        "backend.main:app", 
        host=settings.BACKEND_HOST, 
        port=settings.BACKEND_PORT, 
        reload=reload
    )

# Update app with lifespan handler
app.router.lifespan_context = lifespan

if __name__ == "__main__":
    main()