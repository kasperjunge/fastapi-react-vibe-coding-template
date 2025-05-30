from collections.abc import AsyncGenerator

from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from backend.settings import settings

Base = declarative_base()

def create_database_engine():
    """Create database engine with appropriate settings based on database type."""
    if settings.DATABASE_TYPE.lower() == "sqlite":
        # SQLite-specific engine configuration
        return create_async_engine(
            settings.DATABASE_URL,
            connect_args={"check_same_thread": False},
            echo=settings.ENVIRONMENT == "dev"
        )
    elif settings.DATABASE_TYPE.lower() == "postgresql":
        # PostgreSQL-specific engine configuration
        return create_async_engine(
            settings.DATABASE_URL,
            echo=settings.ENVIRONMENT == "dev"
        )
    else:
        raise ValueError(f"Unsupported database type: {settings.DATABASE_TYPE}")

engine = create_database_engine()
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session