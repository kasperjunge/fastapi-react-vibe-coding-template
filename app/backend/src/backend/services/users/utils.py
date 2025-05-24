from backend.services.users.models import User, UserRole, UserStatus
from backend.services.users.service import UserService
from backend.settings import settings
from backend.services.auth.utils import hash_password
from sqlmodel import Session

def create_admin_user(db: Session):

    existing_admin = db.query(User).filter(User.email == settings.ADMIN_EMAIL).first()
    
    if existing_admin:
        return existing_admin
    
    user = User(
        email=settings.ADMIN_EMAIL,
        username=settings.ADMIN_USERNAME,
        hashed_password=hash_password(settings.ADMIN_PASSWORD),
        role=UserRole.ADMIN,
        status=UserStatus.ACTIVE,
        is_verified=True,
    )
    user = UserService().create_user(user, db)
    
    return user