import uuid
from typing import Optional
from datetime import datetime
from fastapi_users import schemas
    
class UserRead(schemas.BaseUser[uuid.UUID]):
    id: uuid.UUID
    email: str
    is_active: bool
    is_superuser: bool
    is_verified: bool
    created_at: datetime

class UserCreate(schemas.BaseUserCreate):
    password: str
    email: str
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

class UserUpdate(schemas.BaseUserUpdate):
    password: Optional[str] = None
    email: Optional[str] = None
    is_active: Optional[bool] = None
    is_superuser: Optional[bool] = None
    is_verified: Optional[bool] = None