import uuid
from typing import Optional
from fastapi import Request
from fastapi_users import BaseUserManager, UUIDIDMixin

from backend.services.users.models import User
from backend.settings import settings

class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    reset_password_token_secret = settings.SECRET_KEY
    verification_token_secret = settings.SECRET_KEY

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")

    async def on_after_login(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has logged in.")

    async def on_after_update(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has updated their account.")

    async def on_after_delete(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has deleted their account.")
        
    async def on_after_verify(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has verified their account.")

    async def on_after_reset_password(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has reset their password.")
        