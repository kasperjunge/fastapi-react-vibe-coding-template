import os
import sys
from pathlib import Path

from alembic.config import Config
from alembic import command
from sqlmodel import Session, SQLModel, create_engine
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from backend.settings import settings

# Create the SQLAlchemy engine
engine = create_engine(
    settings.DATABASE_URL,
    echo=False,
    pool_pre_ping=True,
    pool_recycle=300,
)

# Asynchronous engine and session for FastAPI Users
async_engine = create_async_engine(
    settings.ASYNC_DATABASE_URL,
    echo=False,
    pool_pre_ping=True,
    pool_recycle=300,
)

AsyncSessionMaker = async_sessionmaker(async_engine, expire_on_commit=False)


def create_db_and_tables() -> None:
    """Create all the tables defined in SQLModel models."""
    SQLModel.metadata.create_all(engine)

async def create_db_and_tables_async() -> None:
    async with async_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


def get_db() -> Session:
    """Get a database session."""
    with Session(engine) as session:
        yield session


async def get_async_db() -> AsyncSession:
    """Get an asynchronous database session."""
    async with AsyncSessionMaker() as session:
        yield session


def run_migrations() -> None:
    """
    Run database migrations using Alembic.
    This function can be imported and called from other parts of the application.
    """
    # Get the path to the alembic.ini file
    alembic_ini = Path(__file__).parents[2] / "alembic.ini"
    
    if not alembic_ini.exists():
        print(f"Error: alembic.ini not found at {alembic_ini}")
        return
    
    # Create Alembic configuration
    alembic_cfg = Config(str(alembic_ini))
    
    # Run the migration
    try:
        command.upgrade(alembic_cfg, "head")
        print("Database migrations completed successfully")
    except Exception as e:
        print(f"Error running database migrations: {e}")
        raise
