import uuid
from typing import Optional
from fastapi import Request, Response
from fastapi_users import BaseUserManager, UUIDIDMixin

from backend.services.users.models import User
from backend.settings import settings
from backend.services.email.service import email_service

class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    reset_password_token_secret = settings.SECRET_KEY
    verification_token_secret = settings.SECRET_KEY

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")
        # Request verification token generation and send email
        await self.request_verify(user, request)

    async def on_after_request_verify(self, user: User, token: str, request: Optional[Request] = None):
        print(f"Verification requested for user {user.id}. Verification token: {token}")
        # Send verification email with the generated token
        await email_service.send_verification_email(
            email=user.email,
            token=token,
            user_name=getattr(user, 'first_name', 'User') or 'User'
        )

    async def on_after_login(self, user: User, request: Optional[Request] = None, response: Optional[Response] = None):
        print(f"User {user.id} has logged in.")

    async def on_after_update(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has updated their account.")

    async def on_after_delete(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has deleted their account.")
        
    async def on_after_verify(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has verified their account.")
        # Send welcome email after verification
        await email_service.send_welcome_email(
            email=user.email,
            user_name=getattr(user, 'first_name', 'User') or 'User'
        )

    async def on_after_reset_password(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has reset their password.")
        