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
  - `settings.py` - Configuration and environment variables with database independence
  - `db.py` - Database configuration with SQLite/PostgreSQL support
  - `services/` - Business logic services
    - `auth/` - Authentication services
    - `users/` - User management services
    - `email/` - Email service for verification
    - `example_service/` - Template service structure

### Frontend Structure (`frontend/`)
- `package.json` - Node.js dependencies and scripts
- `src/` - React application source code
  - `App.tsx` - Main application with React Router and auth context
  - `main.tsx` - Application entry point
  - `components/` - React components
    - `ui/` - Reusable UI components (Button, etc.)
    - `auth/` - Authentication-related components
  - `lib/` - Utility libraries
  - `assets/` - Static assets

### User Service (`backend/src/backend/services/users/`)
- `models.py` - User SQLAlchemy model (extends SQLAlchemyBaseUserTableUUID)
- `service.py` - UserManager class with FastAPI-Users integration and fixed method signatures
- `routes.py` - User-related API endpoints
- `schemas.py` - Pydantic schemas for user data
- `dependencies.py` - Dependency injection for user services

### Email Service (`backend/src/backend/services/email/`)
- `service.py` - EmailService class with multi-provider support
- `__init__.py` - Package initialization
- `templates/` - Email templates directory
  - `verification_email.html` - Professional verification email template
  - `welcome_email.html` - Welcome email after successful verification

### Auth Components (`frontend/src/components/auth/`)
- `RegisterForm.tsx` - User registration with verification notice and login link
- `LoginForm.tsx` - User login with JWT token handling
- `VerificationStatus.tsx` - Email verification status and resend functionality
- `VerifyEmail.tsx` - Handles verification links from emails
- `SuccessPage.tsx` - Success page for completed operations
- `ErrorPage.tsx` - Error page with recovery options

### Main Components (`frontend/src/components/`)
- `Dashboard.tsx` - User dashboard for verified users
- `ui/button.tsx` - Reusable button component

## 🔧 Current Implementation

### Backend Dependencies (pyproject.toml)
- **FastAPI**: Core web framework
- **FastAPI-Users**: Authentication and user management
- **SQLAlchemy**: ORM with database independence
- **Database Drivers**: 
  - `asyncpg`: PostgreSQL async driver
  - `aiosqlite`: SQLite async driver
- **Pydantic**: Data validation and settings
- **Alembic**: Database migrations (works with both database types)
- **JWT**: Token-based authentication
- **fastapi-mail**: Email sending functionality
- **jinja2**: Email template rendering
- **httpx**: HTTP client for Resend API

### Frontend Dependencies (package.json)
- **React**: Frontend framework with TypeScript
- **React Router**: Client-side routing
- **Tailwind CSS**: Utility-first CSS framework
- **Vite**: Build tool and development server
- **Radix UI**: Accessible UI components
- **Lucide React**: Icon library

### Database Configuration

#### Database Independence Features
- **Dynamic database selection**: Environment variable `DATABASE_TYPE` controls selection
- **Automatic driver selection**: Correct SQLAlchemy drivers based on database type
- **Connection string generation**: Automatic based on database type
- **Migration compatibility**: Alembic works with both database types

#### SQLite Configuration (Default)
- **Driver**: `sqlite+aiosqlite`
- **File location**: Configurable via `SQLITE_DB_PATH` (default: `./data/app.db`)
- **Auto-creation**: Database file and directory created automatically
- **Use cases**: Development, testing, small single-user applications

#### PostgreSQL Configuration
- **Driver**: `postgresql+asyncpg`
- **Connection**: Standard PostgreSQL connection parameters
- **Use cases**: Production, multi-user applications, development with production-like environment

### User Model Features
- Inherits from `SQLAlchemyBaseUserTableUUID` (includes `is_verified` field)
- Custom `created_at` timestamp field
- UUID-based primary keys
- **Database agnostic**: Works with both SQLite and PostgreSQL

### UserManager Configuration
- Reset password token secret configured
- Verification token secret configured
- Event handlers for user lifecycle (register, login, verify, etc.)
- ✅ Email verification integrated with `on_after_register`
- ✅ Welcome email integrated with `on_after_verify`
- ✅ Fixed method signatures to match FastAPI Users expectations (includes response parameter)

### Settings Configuration
- **Database Independence**: `DATABASE_TYPE` setting controls database selection
- **SQLite Settings**: `SQLITE_DB_PATH` for database file location
- **PostgreSQL Settings**: Standard connection parameters with defaults
- **Backward Compatibility**: Existing PostgreSQL configurations continue to work
- Environment-based configuration with `.env` file support
- Database connection strings (async and sync) generated dynamically
- Admin user configuration
- Frontend/backend host and port settings
- Secret key for JWT tokens
- ✅ Email configuration (SMTP, provider settings, credentials)
- ✅ Verification token expiration settings

### Database Engine Configuration
- **SQLite Engine**: Configured with `check_same_thread=False` for async operations
- **PostgreSQL Engine**: Standard async configuration
- **Environment-based logging**: SQL query logging enabled in development
- **Error handling**: Proper validation for unsupported database types

### Frontend Authentication Flow
- **React Router**: Handles routing with protected routes
- **Auth Context**: Global user state management with React Context
- **Token Management**: Automatic token validation and storage in localStorage
- **Route Protection**: Redirects based on verification status
- **Complete Flow**: Login → Dashboard (for verified users) or Verification Status (for unverified)

## 🎯 Email Verification Implementation

### ✅ Backend Services
- `EmailService` class with multi-provider support (MailHog, Gmail, Resend)
- Professional HTML email templates with responsive design
- UserManager integration for automatic email sending
- Verification token generation and validation

### ✅ Frontend Components
- **Registration Flow**: Form with validation, verification notice, and login link
- **Login Flow**: Form with JWT token handling and automatic user info retrieval
- **Verification Status**: Page showing verification instructions and resend functionality
- **Email Handler**: Processes verification links from emails
- **Success/Error Pages**: Comprehensive feedback for all scenarios
- **Dashboard**: Protected area for verified users

### ✅ Configuration
- Email provider settings (MailHog for dev, Resend for prod)
- Email template paths and Jinja2 environment
- Verification token expiration (24 hours)
- Rate limiting for resend requests (60-second cooldown)

## 🔗 Key Integration Points

### FastAPI-Users Integration
- User model extends proper base class with `is_verified` field
- UserManager has verification token configuration and correct method signatures
- Verification routes automatically available at `/auth/verify` and `/auth/request-verify-token`
- Email sending implemented in `on_after_register` and `on_after_verify` methods
- ✅ Login functionality working with proper `on_after_login` method signature

### Database Schema
- User table has `is_verified` boolean field (from base class)
- **Database agnostic schema**: Works with both SQLite and PostgreSQL
- **Migration compatibility**: Single migration files work with both database types
- No additional database changes needed for verification

### Authentication Flow
- Registration → Email verification → Login → Dashboard access
- Alternative: Login → Verification Status (if not verified) → Dashboard (after verification)
- Mandatory verification before allowing full app access
- Automatic redirects based on user verification status
- ✅ Complete flow working end-to-end

### API Endpoints
- `POST /api/auth/register` - User registration
- `POST /api/auth/verify` - Email verification with token
- `POST /api/auth/request-verify-token` - Resend verification email
- `POST /api/auth/jwt/login` - User login (returns JWT token) ✅ Working
- `POST /api/auth/jwt/logout` - User logout
- `GET /api/users/me` - Get current user information (requires auth)

### Frontend Routes
- `/register` - Registration form with login link
- `/login` - Login form with registration link
- `/verification-status` - Verification instructions and resend
- `/verify-email/:token` - Verification link handler
- `/success` - Success page for completed operations
- `/error` - Error page with recovery options
- `/dashboard` - Protected dashboard for verified users

## 🐛 Recent Fixes

### ✅ UserManager Method Signature Fix
**Issue**: `TypeError: UserManager.on_after_login() takes from 2 to 3 positional arguments but 4 were given`

**Root Cause**: FastAPI Users was calling `on_after_login` with `user`, `request`, and `response` parameters, but the method was only defined to accept `user` and `request`.

**Solution**: Updated method signature to include the `response` parameter:
```python
# Before (causing error)
async def on_after_login(self, user: User, request: Optional[Request] = None):

# After (working correctly)  
async def on_after_login(self, user: User, request: Optional[Request] = None, response: Optional[Response] = None):
```

**Files Modified**: `backend/src/backend/services/users/service.py`
- Added `Response` import from FastAPI
- Updated `on_after_login` method signature

**Status**: ✅ Fixed - Login endpoint now working correctly

## 🗄️ Database Switching Guide

### Environment Configuration
```bash
# SQLite (default)
DATABASE_TYPE=sqlite
SQLITE_DB_PATH=./data/app.db

# PostgreSQL
DATABASE_TYPE=postgresql
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=secret
```

### Migration Process
1. Update `DATABASE_TYPE` in `.env` file
2. Configure appropriate database settings
3. Run migrations: `uv run alembic upgrade head`
4. Restart application

### Testing Configuration
- **Test database**: In-memory SQLite for fast test execution
- **Test fixtures**: Database-agnostic test setup
- **Test isolation**: Each test gets a fresh database instance

## 📚 Documentation Files
- `agent/DATABASE_CONFIG_EXAMPLES.md` - Comprehensive database configuration examples
- `agent/CURRENT_TASK.md` - Current development task tracking
- `agent/CODEBASE.md` - This file (codebase documentation)
- `README.md` - Main project documentation with database options
