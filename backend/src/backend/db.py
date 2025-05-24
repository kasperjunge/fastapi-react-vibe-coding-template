from collections.abc import AsyncGenerator

from sqlmodel import SQLModel, AsyncSession, async_sessionmaker, create_async_engine
from fastapi import Depends
from fastapi_users.db import SQLAlchemyUserDatabase

from backend.settings import settings
from backend.services.users.models import User

engine = create_async_engine(settings.DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session

async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)