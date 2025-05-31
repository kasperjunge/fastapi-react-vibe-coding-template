# Environment Configuration Guide

This guide explains how to configure your FastAPI-React application for different environments (local development vs production) with the improved settings system.

## 🎯 Problem Solved

The new configuration system addresses the common issue where:
- **Local Development**: Frontend runs on `localhost:5173`, Backend on `localhost:8000` (separate ports)
- **Production**: Frontend and Backend run on the same domain (e.g., `https://example.com` and `https://example.com/api`)

## 🏗️ Architecture Overview

### Local Development
```
Frontend (localhost:5173) ──HTTP──> Backend (localhost:8000)
                          ↑
                    Vite Proxy (/api)
```

### Production (Same Domain)
```
https://example.com ──────> Frontend (Static Files)
https://example.com/api ──> Backend (FastAPI)
```

## 📁 Environment Files

### 1. Local Development (`.env`)
Copy from `env.local.example`:

```bash
ENVIRONMENT=dev
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

# Security
SECRET_KEY=dev-secret-key-change-for-production

# Admin User
ADMIN_EMAIL=admin@example.com
ADMIN_USERNAME=admin
ADMIN_PASSWORD=admin123
ADMIN_FIRST_NAME=Admin
ADMIN_LAST_NAME=User

# Email (MailHog for local development)
EMAIL_PROVIDER=mailhog
MAIL_PORT=1025
MAIL_SERVER=localhost
VERIFICATION_TOKEN_EXPIRE_HOURS=24
```

### 2. Production (`.env`)
Copy from `env.production.example`:

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

# Security
SECRET_KEY=very-secure-secret-key-for-production-32-chars-min

# Admin User
ADMIN_EMAIL=admin@example.com
ADMIN_USERNAME=admin
ADMIN_PASSWORD=SecureAdminPassword123!
ADMIN_FIRST_NAME=Admin
ADMIN_LAST_NAME=User

# Email (Resend for production)
EMAIL_PROVIDER=resend
RESEND_API_KEY=your-resend-api-key-here
MAIL_FROM=noreply@example.com
MAIL_FROM_NAME=Your App Name
```

## 🔧 How It Works

### Backend Settings (Automatic URL Generation)

The improved `settings.py` automatically generates the correct URLs based on environment:

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

@computed_field
@property
def FRONTEND_URL(self) -> str:
    """Generate frontend URL based on environment."""
    if self.IS_PRODUCTION and self.DOMAIN:
        # Production: https://example.com
        base_url = f"{self.PROTOCOL}://{self.DOMAIN}"
        return f"{base_url}{self.FRONTEND_PATH}" if self.FRONTEND_PATH else base_url
    else:
        # Development: http://localhost:5173
        return f"{self.PROTOCOL}://{self.FRONTEND_HOST}:{self.FRONTEND_PORT}"

@computed_field
@property
def API_URL(self) -> str:
    """Generate API URL for frontend consumption."""
    if self.IS_PRODUCTION and self.DOMAIN:
        # Production: "/api" (relative path)
        return self.BACKEND_PATH if self.BACKEND_PATH else ""
    else:
        # Development: "http://localhost:8000" (full URL)
        return self.BACKEND_URL
```

### Frontend API Client

The new `frontend/src/lib/api.ts` handles URL resolution automatically:

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

### CORS Configuration

CORS origins are automatically generated based on environment:

```python
@computed_field
@property
def CORS_ORIGINS(self) -> list[str]:
    """Generate CORS origins list."""
    if self.ALLOWED_ORIGINS:
        return [origin.strip() for origin in self.ALLOWED_ORIGINS.split(",")]
    
    # Auto-generate based on environment
    origins = []
    
    if not self.IS_PRODUCTION:
        # Development: include common development URLs
        origins.extend([
            f"http://localhost:{self.FRONTEND_PORT}",
            f"http://127.0.0.1:{self.FRONTEND_PORT}",
            "http://localhost:3000",  # Common React dev port
            "http://127.0.0.1:3000",
        ])
    
    # Always include the configured frontend URL
    if self.FRONTEND_URL not in origins:
        origins.append(self.FRONTEND_URL)
        
    return origins
```

## 🚀 Usage Examples

### Local Development

1. **Copy environment file:**
   ```bash
   cp env.local.example .env
   ```

2. **Start development servers:**
   ```bash
   # Terminal 1: Backend
   cd backend
   uv run backend

   # Terminal 2: Frontend  
   cd frontend
   npm run dev
   ```

3. **URLs:**
   - Frontend: `http://localhost:5173`
   - Backend: `http://localhost:8000`
   - API calls: `/api/*` (proxied by Vite to backend)

### Production Deployment

1. **Copy environment file:**
   ```bash
   cp env.production.example .env
   ```

2. **Configure your domain:**
   ```bash
   DOMAIN=yourdomain.com
   BACKEND_PATH=/api
   FRONTEND_PATH=
   USE_SSL=true
   ```

3. **Build and deploy:**
   ```bash
   # Build frontend
   cd frontend
   npm run build

   # Deploy both to same domain
   # Frontend: https://yourdomain.com
   # Backend: https://yourdomain.com/api
   ```

## 🔍 Environment Variables Reference

### Core Configuration
- `ENVIRONMENT`: `dev`, `prod`, or `staging`
- `DATABASE_TYPE`: `sqlite` or `postgresql`

### Server Configuration (Development)
- `BACKEND_HOST`: Backend host (default: `localhost`)
- `BACKEND_PORT`: Backend port (default: `8000`)
- `FRONTEND_HOST`: Frontend host (default: `localhost`)
- `FRONTEND_PORT`: Frontend port (default: `5173`)

### Domain Configuration (Production)
- `DOMAIN`: Your production domain (e.g., `example.com`)
- `BACKEND_PATH`: API path (e.g., `/api`)
- `FRONTEND_PATH`: Frontend path (usually empty for root)
- `USE_SSL`: Enable HTTPS (auto-enabled for production)

### CORS Configuration
- `ALLOWED_ORIGINS`: Comma-separated list of allowed origins (auto-generated if empty)

## 🛠️ Migration from Old Setup

If you're migrating from the old configuration:

1. **Remove old variables:**
   - `VITE_API_URL` (now auto-generated)

2. **Add new variables:**
   - `DOMAIN` (for production)
   - `BACKEND_PATH` (for production)
   - `FRONTEND_PATH` (for production)
   - `USE_SSL` (for production)

3. **Update frontend code:**
   - Replace direct `fetch('/api/...')` calls with the new API client:
   ```typescript
   import { api } from '@/lib/api'
   
   // Old
   fetch('/api/auth/login', { ... })
   
   // New
   api.postForm('/auth/login', formData)
   ```

## 🔒 Security Considerations

1. **Secret Keys**: Always use strong, unique secret keys in production
2. **CORS**: The system auto-generates appropriate CORS settings
3. **SSL**: Automatically enabled for production when `DOMAIN` is set
4. **Database**: Use PostgreSQL for production, SQLite for development

## 🐛 Troubleshooting

### CORS Issues
- Check that `ALLOWED_ORIGINS` includes your frontend URL
- Verify that the frontend is making requests to the correct API URL

### API Connection Issues
- In development: Ensure Vite proxy is working (`/api` routes)
- In production: Verify that `BACKEND_PATH` matches your server configuration

### Environment Detection
- Check that `ENVIRONMENT` is set correctly
- Verify that `DOMAIN` is set for production deployments

## 📚 Additional Resources

- [FastAPI CORS Documentation](https://fastapi.tiangolo.com/tutorial/cors/)
- [Vite Proxy Configuration](https://vitejs.dev/config/server-options.html#server-proxy)
- [Environment Variables in Vite](https://vitejs.dev/guide/env-and-mode.html) 