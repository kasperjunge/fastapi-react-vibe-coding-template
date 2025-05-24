from fastapi_users.db import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase
from sqlmodel import Field, SQLModel, Column, String
from datetime import datetime

class User(SQLAlchemyBaseUserTableUUID, SQLModel, table=True):
    email: str = Field(sa_column=Column(String, unique=True, index=True))
    hashed_password: str = Field(sa_column=Column(String))
    is_active: bool = Field(default=True)
    is_superuser: bool = Field(default=False)
    is_verified: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.utcnow)