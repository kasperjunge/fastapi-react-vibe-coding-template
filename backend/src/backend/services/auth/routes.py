from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session

from backend.db import get_db

from .schemas import UserRead, UserCreate, Token
from .service import AuthService

router = APIRouter(prefix="/auth")
service = AuthService()


@router.post("/register", response_model=UserRead)
def register(user: UserCreate, db: Session = Depends(get_db)):
    try:
        new_user = service.create_user(db, user.email, user.password)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc))
    return UserRead.model_validate(new_user)


@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = service.authenticate(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    token = service.create_token_for_user(user)
    return Token(access_token=token)


@router.get("/verify/{token}")
def verify_email(token: str, db: Session = Depends(get_db)):
    if not service.verify_email(db, token):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid token")
    return {"status": "verified"}


@router.post("/request-password-reset")
def request_password_reset(email: str, db: Session = Depends(get_db)):
    token = service.request_password_reset(db, email)
    if not token:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return {"reset_token": token}


@router.post("/reset-password")
def reset_password(token: str, new_password: str, db: Session = Depends(get_db)):
    if not service.reset_password(db, token, new_password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid token")
    return {"status": "password_reset"}
