import asyncio
from typing import List, Optional
from fastapi import HTTPException
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from jinja2 import Environment, FileSystemLoader
import pathlib
import httpx

from backend.settings import settings


class EmailService:
    def __init__(self):
        self.templates_dir = pathlib.Path(__file__).parent / "templates"
        self.jinja_env = Environment(loader=FileSystemLoader(str(self.templates_dir)))
        
        # Configure email based on provider
        if settings.EMAIL_PROVIDER == "mailhog":
            self.mail_config = ConnectionConfig(
                MAIL_USERNAME="",
                MAIL_PASSWORD="",
                MAIL_FROM=settings.MAIL_FROM or "noreply@localhost",
                MAIL_PORT=1025,  # MailHog SMTP port
                MAIL_SERVER="localhost",
                MAIL_FROM_NAME=settings.MAIL_FROM_NAME,
                MAIL_STARTTLS=False,
                MAIL_SSL_TLS=False,
                USE_CREDENTIALS=False,
                VALIDATE_CERTS=False,
                TEMPLATE_FOLDER=str(self.templates_dir)
            )
        elif settings.EMAIL_PROVIDER == "gmail":
            self.mail_config = ConnectionConfig(
                MAIL_USERNAME=settings.MAIL_USERNAME,
                MAIL_PASSWORD=settings.MAIL_PASSWORD,
                MAIL_FROM=settings.MAIL_FROM,
                MAIL_PORT=587,
                MAIL_SERVER="smtp.gmail.com",
                MAIL_FROM_NAME=settings.MAIL_FROM_NAME,
                MAIL_STARTTLS=True,
                MAIL_SSL_TLS=False,
                USE_CREDENTIALS=True,
                VALIDATE_CERTS=True,
                TEMPLATE_FOLDER=str(self.templates_dir)
            )
        else:  # Default to custom SMTP settings
            self.mail_config = ConnectionConfig(
                MAIL_USERNAME=settings.MAIL_USERNAME,
                MAIL_PASSWORD=settings.MAIL_PASSWORD,
                MAIL_FROM=settings.MAIL_FROM,
                MAIL_PORT=settings.MAIL_PORT,
                MAIL_SERVER=settings.MAIL_SERVER,
                MAIL_FROM_NAME=settings.MAIL_FROM_NAME,
                MAIL_STARTTLS=settings.MAIL_STARTTLS,
                MAIL_SSL_TLS=settings.MAIL_SSL_TLS,
                USE_CREDENTIALS=settings.USE_CREDENTIALS,
                VALIDATE_CERTS=settings.VALIDATE_CERTS,
                TEMPLATE_FOLDER=str(self.templates_dir)
            )
        
        self.fastmail = FastMail(self.mail_config)

    async def send_verification_email(self, email: str, token: str, user_name: str = "User"):
        """Send email verification email"""
        try:
            if settings.EMAIL_PROVIDER == "resend":
                await self._send_with_resend(
                    to_email=email,
                    subject="Verify Your Email Address",
                    template_name="verification_email.html",
                    template_data={
                        "user_name": user_name,
                        "verification_link": f"{settings.VITE_API_URL}/verify-email?token={token}",
                        "app_name": settings.MAIL_FROM_NAME
                    }
                )
            else:
                # Use FastMail for MailHog, Gmail, or custom SMTP
                template = self.jinja_env.get_template("verification_email.html")
                html_content = template.render(
                    user_name=user_name,
                    verification_link=f"{settings.VITE_API_URL}/verify-email?token={token}",
                    app_name=settings.MAIL_FROM_NAME
                )
                
                message = MessageSchema(
                    subject="Verify Your Email Address",
                    recipients=[email],
                    body=html_content,
                    subtype=MessageType.html
                )
                
                await self.fastmail.send_message(message)
                
        except Exception as e:
            print(f"Failed to send verification email to {email}: {str(e)}")
            # Don't raise exception to prevent registration failure
            # In production, you might want to log this properly

    async def send_welcome_email(self, email: str, user_name: str = "User"):
        """Send welcome email after successful verification"""
        try:
            if settings.EMAIL_PROVIDER == "resend":
                await self._send_with_resend(
                    to_email=email,
                    subject="Welcome! Your Account is Verified",
                    template_name="welcome_email.html",
                    template_data={
                        "user_name": user_name,
                        "app_name": settings.MAIL_FROM_NAME,
                        "login_link": settings.VITE_API_URL
                    }
                )
            else:
                template = self.jinja_env.get_template("welcome_email.html")
                html_content = template.render(
                    user_name=user_name,
                    app_name=settings.MAIL_FROM_NAME,
                    login_link=settings.VITE_API_URL
                )
                
                message = MessageSchema(
                    subject="Welcome! Your Account is Verified",
                    recipients=[email],
                    body=html_content,
                    subtype=MessageType.html
                )
                
                await self.fastmail.send_message(message)
                
        except Exception as e:
            print(f"Failed to send welcome email to {email}: {str(e)}")

    async def _send_with_resend(self, to_email: str, subject: str, template_name: str, template_data: dict):
        """Send email using Resend API"""
        if not settings.RESEND_API_KEY:
            raise HTTPException(status_code=500, detail="Resend API key not configured")
        
        template = self.jinja_env.get_template(template_name)
        html_content = template.render(**template_data)
        
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "https://api.resend.com/emails",
                headers={
                    "Authorization": f"Bearer {settings.RESEND_API_KEY}",
                    "Content-Type": "application/json"
                },
                json={
                    "from": f"{settings.MAIL_FROM_NAME} <{settings.MAIL_FROM}>",
                    "to": [to_email],
                    "subject": subject,
                    "html": html_content
                }
            )
            
            if response.status_code != 200:
                raise HTTPException(
                    status_code=500, 
                    detail=f"Failed to send email via Resend: {response.text}"
                )


# Global email service instance
email_service = EmailService() 