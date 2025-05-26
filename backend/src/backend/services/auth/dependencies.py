from fastapi_users.authentication import JWTStrategy

from backend.settings import settings

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=settings.SECRET_KEY, lifetime_seconds=3600)