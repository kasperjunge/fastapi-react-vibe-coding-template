from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from sqlalchemy import Column, String, DateTime
from datetime import datetime

from backend.db import Base

class User(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = "user"
    
    created_at = Column(DateTime, default=datetime.utcnow)