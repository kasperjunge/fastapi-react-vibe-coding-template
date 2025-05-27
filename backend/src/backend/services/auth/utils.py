import uuid

from fastapi_users.authentication import AuthenticationBackend, BearerTransport
from fastapi_users import FastAPIUsers

from backend.services.users.models import User
from backend.services.users.dependencies import get_user_manager
from backend.services.auth.dependencies import get_jwt_strategy

bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")

auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [auth_backend],
)

