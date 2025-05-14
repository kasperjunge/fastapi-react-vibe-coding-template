from datetime import datetime, timedelta
from typing import Any, Dict, Optional, Union
from uuid import UUID

from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlmodel import Session, select

from backend.database import get_session
from backend.services.users.models import User
from backend.settings import settings
from backend.services.auth.schemas import TokenData

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    """
    Hash a password using bcrypt
    
    Args:
        password: Plain text password
        
    Returns:
        Hashed password
    """
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a password against its hash
    
    Args:
        plain_password: Plain text password
        hashed_password: Hashed password
        
    Returns:
        True if the password matches the hash, False otherwise
    """
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(
    data: Dict[str, Any], 
    expires_delta: Optional[timedelta] = None
) -> str:
    """
    Create a new JWT access token
    
    Args:
        data: Data to encode in the token
        expires_delta: Token expiration time, defaults to settings value
        
    Returns:
        Encoded JWT token as string
    """
    to_encode = data.copy()
    
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES
        )
    
    to_encode.update({"exp": expire})
    
    return jwt.encode(
        to_encode, 
        settings.JWT_SECRET_KEY, 
        algorithm=settings.JWT_ALGORITHM
    )


def create_refresh_token(
    data: Dict[str, Any],
    expires_delta: Optional[timedelta] = None
) -> str:
    """
    Create a new JWT refresh token
    
    Args:
        data: Data to encode in the token
        expires_delta: Token expiration time, defaults to settings value
        
    Returns:
        Encoded JWT token as string
    """
    to_encode = data.copy()
    
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            days=settings.JWT_REFRESH_TOKEN_EXPIRE_DAYS
        )
    
    to_encode.update({"exp": expire})
    
    return jwt.encode(
        to_encode, 
        settings.JWT_SECRET_KEY, 
        algorithm=settings.JWT_ALGORITHM
    )


def verify_token(token: str) -> Optional[TokenData]:
    """
    Verify and decode a JWT token
    
    Args:
        token: JWT token to verify
        
    Returns:
        TokenData object if valid, None otherwise
        
    Raises:
        HTTPException: If token is invalid
    """
    try:
        payload = jwt.decode(
            token, 
            settings.JWT_SECRET_KEY, 
            algorithms=[settings.JWT_ALGORITHM]
        )
        
        user_id: str = payload.get("sub")
        role: str = payload.get("role", "user")
        exp: datetime = datetime.fromtimestamp(payload.get("exp"))
        
        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
            
        return TokenData(user_id=UUID(user_id), role=role, exp=exp)
        
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )


async def authenticate_user(
    email: str, 
    password: str, 
    session: Session = Depends(get_session)
) -> Optional[User]:
    """
    Authenticate a user with email and password
    
    Args:
        email: User email
        password: User password
        session: Database session
        
    Returns:
        User object if authentication succeeds, None otherwise
    """
    query = select(User).where(User.email == email)
    user = session.exec(query).first()
    
    if not user:
        return None
    
    if not verify_password(password, user.password_hash):
        return None
        
    return user


async def get_current_user(
    token: str, 
    session: Session = Depends(get_session)
) -> Optional[User]:
    """
    Get the current user from a JWT token
    
    Args:
        token: JWT token
        session: Database session
        
    Returns:
        User object if token is valid and user exists
        
    Raises:
        HTTPException: If token is invalid or user doesn't exist
    """
    token_data = verify_token(token)
    
    if not token_data:
        return None
    
    query = select(User).where(User.id == token_data.user_id)
    user = session.exec(query).first()
    
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="User not found"
        )
        
    return user
