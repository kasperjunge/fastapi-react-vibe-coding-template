# Codebase Documentation

## 📁 Project Structure

### Root Directory
- `backend/` - FastAPI backend application
- `frontend/` - React frontend application  
- `agent/` - AI assistant documentation and task tracking
- `docker-compose.yml` - Docker services configuration

### Backend Structure (`backend/`)
- `pyproject.toml` - Python dependencies and project configuration
- `src/backend/` - Main application source code
  - `app.py` - FastAPI application setup
  - `main.py` - Application entry point
  - `settings.py` - Configuration and environment variables
  - `db.py` - Database configuration
  - `services/` - Business logic services
    - `auth/` - Authentication services
    - `users/` - User management services
    - `example_service/` - Template service structure

### User Service (`backend/src/backend/services/users/`)
- `models.py` - User SQLAlchemy model (extends SQLAlchemyBaseUserTableUUID)
- `service.py` - UserManager class with FastAPI-Users integration
- `routes.py` - User-related API endpoints
- `schemas.py` - Pydantic schemas for user data
- `dependencies.py` - Dependency injection for user services

### Email Service (`backend/src/backend/services/email/`)
- `service.py` - EmailService class with multi-provider support
- `__init__.py` - Package initialization
- `templates/` - Email templates directory
  - `verification_email.html` - Professional verification email template
  - `welcome_email.html` - Welcome email after successful verification

## 🔧 Current Implementation

### Dependencies (pyproject.toml)
- **FastAPI**: Core web framework
- **FastAPI-Users**: Authentication and user management
- **SQLAlchemy**: ORM with PostgreSQL support
- **Pydantic**: Data validation and settings
- **Alembic**: Database migrations
- **JWT**: Token-based authentication

### User Model Features
- Inherits from `SQLAlchemyBaseUserTableUUID` (includes `is_verified` field)
- Custom `created_at` timestamp field
- UUID-based primary keys

### UserManager Configuration
- Reset password token secret configured
- Verification token secret configured
- Event handlers for user lifecycle (register, login, verify, etc.)
- ✅ Email verification integrated with `on_after_register`
- ✅ Welcome email integrated with `on_after_verify`

### Settings Configuration
- Environment-based configuration with `.env` file support
- Database connection strings (async and sync)
- Admin user configuration
- Frontend/backend host and port settings
- Secret key for JWT tokens
- ✅ Email configuration (SMTP, provider settings, credentials)
- ✅ Verification token expiration settings

## 🚧 Missing for Email Verification

### ✅ Dependencies Added
- `fastapi-mail` - Email sending functionality
- `jinja2` - Email template rendering
- `httpx` - HTTP client for Resend API

### ✅ Services Created
- `backend/src/backend/services/email/service.py` - Email service module
- `backend/src/backend/services/email/templates/` - Email templates directory
- MailHog setup as standalone Docker container (see NOTES.md)

### ✅ Configuration Added
- Email provider settings (MailHog, Gmail, Resend API)
- Email template paths and Jinja2 environment
- Verification token expiration settings (24 hours)

### Frontend Components Needed
- Registration form with verification notice
- Email verification status page
- Verification link handler
- Resend verification functionality

## 🔗 Key Integration Points

### FastAPI-Users Integration
- User model already extends proper base class
- UserManager has verification token configuration
- Verification routes should be automatically available
- Need to implement email sending in `on_after_register` method

### Database Schema
- User table has `is_verified` boolean field (from base class)
- No additional database changes needed for basic verification

### Authentication Flow
- Registration → Email verification → Login access
- Verification status check before allowing app access
