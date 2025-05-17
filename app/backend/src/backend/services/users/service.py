from backend.services.users.models import User, UserRole, UserStatus
from backend.services.users.schemas import UserCreate
from backend.db import get_db
from sqlmodel import Session
from backend.settings import settings

class UserService:

    def create_user(self, user: UserCreate, db: Session):
        user = User(**user.model_dump())
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    

def create_admin_user(db: Session):

    existing_admin = db.query(User).filter(User.email == settings.ADMIN_EMAIL).first()
    
    if existing_admin:
        return existing_admin
    
    user = User(
        email=settings.ADMIN_EMAIL,
        username=settings.ADMIN_USERNAME,
        password=settings.ADMIN_PASSWORD,
        role=UserRole.ADMIN,
        status=UserStatus.ACTIVE,
    )
    user = UserService().create_user(user, db)
    return user