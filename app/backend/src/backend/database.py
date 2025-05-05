import os
import sys
from pathlib import Path

from alembic.config import Config
from alembic import command
from sqlmodel import Session, SQLModel, create_engine, select

from backend.settings import settings

# Create the SQLAlchemy engine
engine = create_engine(
    settings.DATABASE_URL,
    echo=False,
    pool_pre_ping=True,  # Check connection before using it
    pool_recycle=300,  # Recycle connections every 5 minutes
)


def create_db_and_tables() -> None:
    """Create all the tables defined in SQLModel models."""
    SQLModel.metadata.create_all(engine)


def get_session() -> Session:
    """Get a database session."""
    with Session(engine) as session:
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
