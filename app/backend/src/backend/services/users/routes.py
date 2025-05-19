from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from backend.services.users.service import UserService
from backend.db import get_db
from backend.services.users.schemas import UserCreate

router = APIRouter(prefix="/users")


@router.post("/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        return UserService().create_user(user, db)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/by-email/{email}")
def get_user_by_email(email: str, db: Session = Depends(get_db)):   

    try:
        user = UserService().get_user_by_email(email, db)
        return user
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

# @router.get("/me")
# def get_current_user():
#     return {"message": "User retrieved successfully"}

# @router.put("/me")
# def update_user():
#     return {"message": "User updated successfully"}

# @router.delete("/me")
# def delete_user():
#     return {"message": "User deleted successfully"}

# @router.get("/")
# def get_users():
#     return {"message": "Users retrieved successfully"}

# @router.get("/{user_id}")
# def get_user():
#     return {"message": "User retrieved successfully"}

# @router.put("/{user_id}")
# def update_user():
#     return {"message": "User updated successfully"}

# @router.delete("/{user_id}")
# def delete_user():
#     return {"message": "User deleted successfully"}


# @router.get("/search")
# def search_users():
#     return {"message": "Users retrieved successfully"}

# @router.get("/username-available/{username}")
# def is_username_available():
#     return {"message": "Username availability checked successfully"}
