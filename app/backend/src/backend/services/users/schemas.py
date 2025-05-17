from pydantic import BaseModel
from backend.services.users.models import UserRole, UserStatus

class UserCreate(BaseModel):
    email: str
    username: str
    password: str
    first_name: str
    last_name: str
    bio: str
    profile_image_url: str
    role: UserRole
    status: UserStatus