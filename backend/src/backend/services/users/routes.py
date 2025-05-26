from fastapi import APIRouter
from backend.services.auth.utils import fastapi_users
from backend.services.users.schemas import UserRead, UserUpdate

router = APIRouter()

router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)