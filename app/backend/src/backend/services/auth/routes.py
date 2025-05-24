from fastapi import APIRouter

from .fastapi_users import fastapi_users, auth_backend

router = APIRouter()

# JWT auth routes
router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

# Registration and verification
router.include_router(
    fastapi_users.get_register_router(),
    prefix="/auth",
    tags=["auth"],
)
router.include_router(
    fastapi_users.get_verify_router(),
    prefix="/auth",
    tags=["auth"],
)
router.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)

# Users router
router.include_router(
    fastapi_users.get_users_router(),
    prefix="/users",
    tags=["users"],
)
