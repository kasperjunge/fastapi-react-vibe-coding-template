from fastapi import Depends

from backend.services.users.service import UserManager
from fastapi_users.db import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession

from backend.db import get_async_session
from backend.services.users.models import User

async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User) 

async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)


