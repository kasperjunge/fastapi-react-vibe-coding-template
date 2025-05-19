from backend.services.users.models import User
from backend.services.users.schemas import UserCreate
from sqlmodel import Session

class UserService:

    def create_user(self, user: UserCreate, db: Session):
        user = User(**user.model_dump())
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    def get_user_by_email(self, email: str, db: Session):
        return db.query(User).filter(User.email == email).first()
    
    def get_user_by_id(self, id: int, db: Session):
        return db.query(User).filter(User.id == id).first()
    
    def get_all_users(self, db: Session):
        return db.query(User).all()