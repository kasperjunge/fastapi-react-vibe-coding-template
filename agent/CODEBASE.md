# Codebase Documentation

This document provides comprehensive technical implementation details for AI agents working on the FastAPI-React template project.

## 📁 Project Structure

### Root Directory
- `backend/` - FastAPI backend application
- `frontend/` - React frontend application  
- `agent/` - AI assistant documentation (this file and related docs)
- `docker-compose.yml` - Docker services configuration

### Backend Structure (`backend/`)
- `pyproject.toml` - Python dependencies and project configuration
- `src/backend/` - Main application source code
  - `app.py` - FastAPI application setup with CORS middleware
  - `main.py` - Application entry point with OpenAPI schema dumping
  - `settings.py` - Configuration and environment variables with computed fields
  - `db.py` - Database configuration with SQLite/PostgreSQL support
  - `services/` - Business logic services
    - `auth/` - Authentication services (FastAPI-Users)
    - `users/` - User management services with email verification
    - `email/` - Email service for verification with multi-provider support
    - `example_service/` - Template service structure

### Frontend Structure (`frontend/`)
- `package.json` - Node.js dependencies and scripts
- `src/` - React application source code
  - `App.tsx` - Main application with React Router and auth context
  - `main.tsx` - Application entry point
  - `components/` - React components
    - `ui/` - Reusable UI components (Button, etc.)
    - `auth/` - Authentication-related components (login, register, verification)
  - `contexts/` - React contexts (AuthContext)
  - `lib/` - Utility libraries
    - `api.ts` - Environment-aware API client

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
- **httpx**: HTTP client for API requests

### Frontend Dependencies (package.json)
- **React**: Frontend framework with TypeScript
- **React Router**: Client-side routing
- **Tailwind CSS**: Utility-first CSS framework
- **Vite**: Build tool and development server
- **Radix UI**: Accessible UI components
- **Lucide React**: Icon library

## 🗄️ Database Configuration

### Database Independence Features
- **Dynamic database selection**: Environment variable `DATABASE_TYPE` controls selection
- **Automatic driver selection**: Correct SQLAlchemy drivers based on database type
- **Connection string generation**: Automatic based on database type
- **Migration compatibility**: Alembic works with both database types

### SQLite Configuration (Default)
- **Driver**: `sqlite+aiosqlite`
- **File location**: Configurable via `SQLITE_DB_PATH` (default: `./data/app.db`)
- **Auto-creation**: Database file and directory created automatically
- **Use cases**: Development, testing, small single-user applications

**Environment Configuration:**
```bash
DATABASE_TYPE=sqlite
SQLITE_DB_PATH=./data/app.db
```

### PostgreSQL Configuration
- **Driver**: `postgresql+asyncpg`
- **Connection**: Standard PostgreSQL connection parameters
- **Use cases**: Production, multi-user applications, development with production-like environment

**Environment Configuration:**
```bash
DATABASE_TYPE=postgresql
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=secret
```

### Database Setup Examples

#### SQLite Setup (Default)
1. No additional setup required
2. Database file will be created automatically at the specified path
3. Directory structure will be created if it doesn't exist

```bash
# Start the application
cd backend
uv run alembic upgrade head
uv run backend
```

#### PostgreSQL Setup with Docker
```bash
# Start PostgreSQL container
docker run --name local-postgres \
  -e POSTGRES_DB=dev_db \
  -e POSTGRES_USER=dev_user \
  -e POSTGRES_PASSWORD=dev_password \
  -p 5432:5432 \
  -v pgdata:/var/lib/postgresql/data \
  -d postgres

# Run migrations and start application
cd backend
uv run alembic upgrade head
uv run backend
```

#### Using Docker Compose
```bash
# From project root
docker-compose up -d db

# Run migrations and start application
cd backend
uv run alembic upgrade head
uv run backend
```

### Migration Commands
```bash
cd backend
# Create new migration
uv run alembic revision --autogenerate -m "Description of changes"

# Apply migrations
uv run alembic upgrade head

# Rollback migration
uv run alembic downgrade -1
```

## ⚙️ Environment Configuration System

### Enhanced Settings Architecture
The `settings.py` file uses Pydantic with computed fields for automatic URL generation:

```python
@computed_field
@property
def BACKEND_URL(self) -> str:
    """Generate backend URL based on environment."""
    if self.IS_PRODUCTION and self.DOMAIN:
        # Production: https://example.com/api
        base_url = f"{self.PROTOCOL}://{self.DOMAIN}"
        return f"{base_url}{self.BACKEND_PATH}" if self.BACKEND_PATH else base_url
    else:
        # Development: http://localhost:8000
        return f"{self.PROTOCOL}://{self.BACKEND_HOST}:{self.BACKEND_PORT}"
```

### Environment Types & Configuration

#### Local Development Configuration
```bash
ENVIRONMENT=local
DATABASE_TYPE=sqlite
SQLITE_DB_PATH=./data/app.db

# Server Configuration
BACKEND_HOST=localhost
BACKEND_PORT=8000
FRONTEND_HOST=localhost
FRONTEND_PORT=5173

# No domain configuration needed
DOMAIN=
BACKEND_PATH=
FRONTEND_PATH=
USE_SSL=false

# Email (MailHog for development)
EMAIL_PROVIDER=mailhog
MAIL_PORT=1025
MAIL_SERVER=localhost
```

#### Production Configuration
```bash
ENVIRONMENT=prod
DATABASE_TYPE=postgresql

# Production Database
POSTGRES_HOST=your-postgres-host.com
POSTGRES_PORT=5432
POSTGRES_DB=prod_db
POSTGRES_USER=prod_user
POSTGRES_PASSWORD=secure-production-password

# Production Domain Configuration
DOMAIN=example.com
BACKEND_PATH=/api
FRONTEND_PATH=
USE_SSL=true

# Email (Resend for production)
EMAIL_PROVIDER=resend
RESEND_API_KEY=your-resend-api-key
MAIL_FROM=noreply@example.com
MAIL_FROM_NAME=Your App Name
```

### Automatic URL Generation
The system automatically generates appropriate URLs:

- **Development**: 
  - Backend URL: `http://localhost:8000`
  - Frontend URL: `http://localhost:5173`
  - API URL: `http://localhost:8000` (full URL for CORS)

- **Production**:
  - Backend URL: `https://example.com/api`
  - Frontend URL: `https://example.com`
  - API URL: `/api` (relative path for same domain)

### CORS Configuration
Automatic CORS origins generation:
- **Development**: Includes `localhost:5173`, `localhost:3000`, `127.0.0.1` variants
- **Production**: Uses configured `ALLOWED_ORIGINS` or restricts to frontend URL

## 👤 User Management & Authentication

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
- ✅ Fixed method signatures to match FastAPI Users expectations

### Settings Configuration Features
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

## 📧 Email System Implementation

### EmailService Architecture
- **Multi-provider support**: MailHog (development), Gmail, Resend (production)
- **Professional HTML templates**: Responsive design with Jinja2 rendering
- **UserManager integration**: Automatic email sending on user events
- **Template system**: `verification_email.html`, `welcome_email.html`

### Email Provider Configurations

#### MailHog (Development)
```bash
EMAIL_PROVIDER=mailhog
MAIL_USERNAME=
MAIL_PASSWORD=
MAIL_FROM=test@test.com
MAIL_PORT=1025
MAIL_SERVER=localhost
MAIL_STARTTLS=false
MAIL_SSL_TLS=false
USE_CREDENTIALS=false
VALIDATE_CERTS=false
```

#### Resend (Production)
```bash
EMAIL_PROVIDER=resend
RESEND_API_KEY=your-resend-api-key
MAIL_FROM=noreply@yourdomain.com
MAIL_FROM_NAME=Your App Name
VERIFICATION_TOKEN_EXPIRE_HOURS=24
```

#### Gmail (Production)
```bash
EMAIL_PROVIDER=gmail
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_STARTTLS=true
MAIL_SSL_TLS=false
USE_CREDENTIALS=true
VALIDATE_CERTS=true
```

## ⚛️ Frontend Architecture

### Authentication Flow Implementation
- **React Router**: Handles routing with protected routes
- **Auth Context**: Global user state management with React Context
- **Token Management**: Automatic token validation and storage in localStorage
- **Route Protection**: Redirects based on verification status
- **Complete Flow**: Login → Dashboard (for verified users) or Verification Status (for unverified)

### API Client Implementation
Environment-aware API client in `frontend/src/lib/api.ts`:

```typescript
export const getApiUrl = (): string => {
  // In development, use the proxy (relative URLs)
  if (import.meta.env.DEV) {
    return '/api'  // Vite proxy handles this
  }
  
  // In production, check if we have a custom API URL
  const apiUrl = import.meta.env.VITE_API_URL
  if (apiUrl) {
    return apiUrl
  }
  
  // Fallback: assume API is at /api relative to current domain
  return '/api'
}
```

### Component Architecture

#### Authentication Components (`frontend/src/components/auth/`)
- `RegisterForm.tsx` - User registration with validation, verification notice, and login link
- `LoginForm.tsx` - User login with JWT token handling and automatic user info retrieval
- `VerificationStatus.tsx` - Page showing verification instructions and resend functionality
- `VerifyEmail.tsx` - Processes verification links from emails
- `SuccessPage.tsx` - Comprehensive feedback for completed operations
- `ErrorPage.tsx` - Error handling with recovery options

#### Main Components
- `Dashboard.tsx` - Protected area for verified users
- `ui/button.tsx` - Reusable button component with Radix UI

## 🔗 Key Integration Points

### FastAPI-Users Integration
- User model extends proper base class with `is_verified` field
- UserManager has verification token configuration and correct method signatures
- Verification routes automatically available at `/auth/verify` and `/auth/request-verify-token`
- Email sending implemented in `on_after_register` and `on_after_verify` methods
- ✅ Login functionality working with proper `on_after_login` method signature

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

## 🛠️ OpenAPI Schema Auto-Generation

### Implementation Details
- **Location**: `backend/src/backend/main.py`
- **Functionality**: Automatically dumps OpenAPI schema to `agent/openapi.json` every time backend starts
- **Trigger**: Runs when executing `uv run backend`
- Uses FastAPI's built-in `app.openapi()` method to generate schema
- Saves to `agent/openapi.json` in project root
- Pretty-formatted JSON with 2-space indentation
- Error handling with console feedback
- UTF-8 encoding for proper character support

### Usage & Benefits
- Always up-to-date API documentation
- Useful for frontend development and API consumers
- Automatic generation without manual intervention
- Stored in agent/ directory for easy access by AI assistant

## 🔧 Development Environment Setup

### Database Engine Configuration
- **SQLite Engine**: Configured with `check_same_thread=False` for async operations
- **PostgreSQL Engine**: Standard async configuration
- **Environment-based logging**: SQL query logging enabled in development
- **Error handling**: Proper validation for unsupported database types

### Vite Configuration Enhancement
```typescript
// vite.config.ts highlights
export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173,
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true
      }
    }
  }
})
```

## 🐛 Known Issues & Fixes

### ✅ UserManager Method Signature Fix (Resolved)
**Issue**: `TypeError: UserManager.on_after_login() takes from 2 to 3 positional arguments but 4 were given`

**Root Cause**: FastAPI Users was calling `on_after_login` with `user`, `request`, and `response` parameters, but the method was only defined to accept `user` and `request`.

**Solution**: Updated method signature to include the `response` parameter:
```python
# Fixed method signature
async def on_after_login(self, user: User, request: Optional[Request] = None, response: Optional[Response] = None):
```

**Status**: ✅ Fixed - Login endpoint now working correctly

## 🗄️ Database Switching Guide

### Migration Process
1. Update `DATABASE_TYPE` in `.env` file
2. Configure appropriate database settings
3. Run migrations: `uv run alembic upgrade head`
4. Restart application

### Troubleshooting Database Issues

#### SQLite Issues
- **Permission errors**: Ensure the application has write access to the database directory
- **Database locked**: Make sure no other processes are accessing the database file
- **Path issues**: Use absolute paths if relative paths cause problems

#### PostgreSQL Issues
- **Connection refused**: Verify PostgreSQL is running and accessible
- **Authentication failed**: Check username, password, and database name
- **Database doesn't exist**: Create the database before running migrations
- **Port conflicts**: Ensure PostgreSQL port (default 5432) is not in use by other services

## 📊 Environment Configuration Analysis

### Security Recommendations
1. **SECRET_KEY**: Must be 32+ characters, cryptographically secure
2. **Admin Password**: Use complex passwords, avoid defaults like "admin123"
3. **Database Credentials**: Use strong passwords in production
4. **Email Configuration**: Use proper SMTP settings and API keys
5. **CORS Settings**: Restrict origins in production environments

### Configuration Best Practices
- Use environment-specific `.env` files
- Validate required environment variables at startup
- Use proper data types (boolean values as `true`/`false`, not strings)
- Separate development and production configurations
- Use secrets management in production (AWS Secrets Manager, etc.)

### Common Configuration Patterns
- **Development**: SQLite + MailHog + relaxed CORS
- **Production**: PostgreSQL + Resend/Gmail + strict CORS + HTTPS
- **Testing**: SQLite + mock email provider + isolated configuration

---

**Last Updated**: Documentation consolidation phase
**Scope**: Comprehensive technical reference for AI agents
**Usage**: Refer to this document for implementation details, database configuration, environment setup, and troubleshooting guidance
