# FastAPI-React Vibe Coding Template

A modern, full-stack web application template featuring FastAPI backend with database independence and React frontend with complete authentication system.

## 📚 Quick Navigation

- [🚀 Features](#-features)
- [📁 Project Structure](#-project-structure) 
- [⚡ Quick Start](#-quick-start)
- [🛠️ Detailed Setup](#️-detailed-setup)
- [🗄️ Database Options](#️-database-options)
- [📧 Email Configuration](#-email-configuration)
- [🧪 Testing](#-testing)
- [🐳 Docker Development](#-docker-development)
- [🔧 Development Commands](#-development-commands)
- [🚀 Deployment](#-deployment)
- [🐛 Troubleshooting](#-troubleshooting)
- [🤝 Contributing](#-contributing)

## 🚀 Features

### Backend ([📖 Backend README](backend/README.md))
- **FastAPI**: High-performance, easy-to-learn, fast to code, ready for production
- **Database Independence**: Support for both SQLite (development) and PostgreSQL (production)
- **SQLAlchemy**: Async SQL database operations with automatic driver selection
- **FastAPI-Users**: Complete authentication system with user management
- **Email Verification**: Complete email verification system with multiple providers
- **Alembic**: Database migrations that work with both database types
- **Pydantic**: Data validation and settings management
- **Service-oriented architecture**: Modular structure for maintainability and scalability
- **Docker support**: Ready for containerized deployment

### Frontend ([📖 Frontend README](frontend/README.md))
- **React 18**: Modern frontend framework with TypeScript
- **Complete Authentication Flow**: Registration, verification, and login system
- **Vite**: Fast build tool and development server with HMR
- **Tailwind CSS**: Utility-first CSS framework with responsive design
- **Radix UI**: Accessible, unstyled components
- **Environment-Aware API Client**: Seamless dev/prod API integration

### Environment & DevOps
- **Automatic URL Generation**: Environment-aware backend/frontend URL configuration
- **CORS Auto-Configuration**: Development and production CORS settings
- **Multiple Environment Support**: Local development, staging, and production configurations
- **Same-Domain Deployment**: Support for frontend and backend on same domain

## 📁 Project Structure

```
fastapi-react-vibe-coding-template/
├── 📁 backend/                    # FastAPI backend
│   ├── 📁 src/backend/           # Source code
│   │   ├── 📁 services/          # Feature-based services
│   │   │   ├── 📁 auth/          # Authentication (FastAPI-Users)
│   │   │   ├── 📁 users/         # User management
│   │   │   ├── 📁 email/         # Email verification service
│   │   │   └── 📁 example_service/ # Example service template
│   │   ├── 📄 app.py             # FastAPI app setup
│   │   ├── 📄 db.py              # Database configuration (SQLite/PostgreSQL)
│   │   ├── 📄 main.py            # Application entry point
│   │   └── 📄 settings.py        # Configuration settings
│   ├── 📁 migrations/            # Alembic database migrations
│   ├── 📁 tests/                 # Comprehensive test suite
│   ├── 📄 pyproject.toml         # Python dependencies (uv)
│   ├── 📄 README.md             # Backend documentation & contributing guide
│   └── 📄 Dockerfile            # Backend container
├── 📁 frontend/                  # React frontend with auth components
│   ├── 📁 src/                   # Frontend source code
│   │   ├── 📁 components/        # React components (auth, UI)
│   │   ├── 📁 contexts/          # React contexts (Auth)
│   │   └── 📁 lib/               # Utilities (API client)
│   ├── 📄 README.md             # Frontend documentation
│   └── 📄 package.json          # Node.js dependencies
├── 📁 agent/                     # AI assistant documentation
│   ├── 📄 CURRENT_TASK.md       # Current project status & ongoing work
│   ├── 📄 CODEBASE.md           # Technical implementation details
│   └── 📄 SCRATCHPAD.md         # Development insights & discoveries
├── 📄 docker-compose.yml         # Multi-service setup
├── 📄 env.example                # Environment template
├── 📄 env.local.example          # Local development template
├── 📄 env.production.example     # Production template
└── 📄 README.md                  # This file - Complete project guide
```

## ⚡ Quick Start

**Prerequisites**: Python 3.12+, Node.js 18+, [uv](https://docs.astral.sh/uv/)

```bash
# 1. Clone and setup
git clone <your-repo-url>
cd fastapi-react-vibe-coding-template
cp env.local.example .env  # Use SQLite by default

# 2. Backend setup
cd backend
uv sync && uv run alembic upgrade head && uv run backend &

# 3. Frontend setup (new terminal)
cd frontend
npm install && npm run dev

# 4. Open in browser
open http://localhost:5173
```

**🎉 That's it!** You now have a fully functional FastAPI-React application with authentication.

## 🛠️ Detailed Setup

### 1. Environment Configuration

Choose your setup based on your needs:

#### Option A: SQLite (Recommended for getting started)
```bash
cp env.local.example .env
# Edit .env if needed - defaults are fine for development
```

#### Option B: PostgreSQL (Production-like setup)
```bash
cp env.example .env
# Edit .env to configure PostgreSQL settings
docker-compose up -d db  # Start PostgreSQL
```

#### Option C: Production Deployment
```bash
cp env.production.example .env
# Configure production settings including:
# - Strong SECRET_KEY (32+ characters)
# - Secure admin password
# - Production database credentials
# - Email provider settings (Resend/Gmail)
# - Domain configuration for same-domain deployment
```

### 2. Backend Setup

```bash
cd backend
uv sync                        # Install dependencies
uv run alembic upgrade head    # Run database migrations
uv run backend                 # Start the backend server
```

**Available at:**
- 🌐 API: `http://localhost:8000`
- 📚 API Docs: `http://localhost:8000/docs`
- 📘 Alternative Docs: `http://localhost:8000/redoc`

### 3. Frontend Setup

```bash
cd frontend
npm install                    # Install dependencies
npm run dev                    # Start the development server
```

**Available at:**
- 🌐 Frontend: `http://localhost:5173`

## 🗄️ Database Options

This template supports seamless switching between databases:

### SQLite (Default)
- ✅ **Pros**: No external dependencies, fast setup, perfect for development
- ⚠️ **Cons**: Single-user, not suitable for production with multiple users
- 🎯 **Use cases**: Development, testing, small single-user applications

**Configuration:**
```bash
DATABASE_TYPE=sqlite
SQLITE_DB_PATH=./data/app.db
```

### PostgreSQL
- ✅ **Pros**: Production-ready, multi-user, advanced features, excellent performance
- ⚠️ **Cons**: Requires external service, more complex setup
- 🎯 **Use cases**: Production, development with production-like environment

**Configuration:**
```bash
DATABASE_TYPE=postgresql
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=secret
```

### Switching Databases
```bash
# 1. Update DATABASE_TYPE in your .env file
# 2. Configure the appropriate database settings
# 3. Run migrations
cd backend && uv run alembic upgrade head
# 4. Restart the application
```

## 📧 Email Configuration

### Development (MailHog)
```bash
# Start MailHog for email testing
docker run -d -p 1025:1025 -p 8025:8025 mailhog/mailhog

# Environment configuration
EMAIL_PROVIDER=mailhog
MAIL_PORT=1025
MAIL_SERVER=localhost
```
Access email interface at `http://localhost:8025`

### Production (Resend)
```bash
EMAIL_PROVIDER=resend
RESEND_API_KEY=your-resend-api-key
MAIL_FROM=noreply@yourdomain.com
MAIL_FROM_NAME=Your App Name
```

### Production (Gmail)
```bash
EMAIL_PROVIDER=gmail
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_STARTTLS=true
```

## 🧪 Testing

### Backend Tests
```bash
cd backend
uv run pytest                  # Run all tests
uv run pytest -v              # Verbose output
uv run pytest --cov           # With coverage report
uv run pytest tests/test_auth.py  # Specific test file
```

**Test Coverage Includes:**
- 🔐 User service tests (registration, verification, authentication)
- 📧 Email service tests (template rendering, sending)
- 🛣️ API endpoint tests (auth flows, protected routes)
- 🔑 Authentication flow tests (JWT, verification)

### Frontend Testing
```bash
cd frontend
npm run type-check             # TypeScript compilation
npm run lint                   # ESLint checks
npm run lint -- --fix         # Fix linting issues
```

## 🐳 Docker Development

### Full Stack
```bash
# Start entire stack
docker-compose up -d

# Stop all services
docker-compose down

# Stop and remove volumes
docker-compose down -v
```

### Individual Services
```bash
docker-compose up -d db        # Database only
docker-compose up -d backend   # Backend only
docker-compose up -d frontend  # Frontend only
```

### PostgreSQL Management
```bash
# Start PostgreSQL container manually
docker run --name local-postgres \
  -e POSTGRES_DB=db \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=secret \
  -p 5432:5432 \
  -v pgdata:/var/lib/postgresql/data \
  -d postgres

# Access PostgreSQL
docker exec -it local-postgres psql -U postgres -d db

# Check connection
docker exec -it local-postgres pg_isready -U postgres
```

## 🔧 Development Commands

### Backend Development
```bash
cd backend

# Dependencies
uv sync                        # Install/update dependencies
uv add package-name            # Add new dependency
uv add --dev package-name      # Add dev dependency

# Database migrations
uv run alembic revision --autogenerate -m "Description"
uv run alembic upgrade head    # Apply migrations
uv run alembic downgrade -1    # Rollback one migration
uv run alembic history         # View migration history

# Development server
uv run backend                 # Start server
uv run uvicorn backend.main:app --reload --log-level debug  # Debug mode

# Testing
uv run pytest                 # All tests
uv run pytest --cov --cov-report=html  # With HTML coverage
uv run pytest -x              # Stop on first failure
```

### Frontend Development
```bash
cd frontend

# Dependencies
npm install                    # Install dependencies
npm install package-name      # Add dependency
npm install --save-dev package-name  # Add dev dependency

# Development
npm run dev                    # Start dev server
npm run build                  # Production build
npm run preview                # Preview production build

# Quality checks
npm run type-check             # TypeScript check
npm run lint                   # ESLint
npm outdated                   # Check for updates
```

### Troubleshooting Commands
```bash
# Clear caches
rm -rf backend/.venv
rm -rf frontend/node_modules frontend/package-lock.json
rm -rf frontend/.vite

# Reset database (development only)
rm -rf backend/migrations/versions/*.py
cd backend && uv run alembic stamp head
cd backend && uv run alembic revision --autogenerate -m "Initial"
cd backend && uv run alembic upgrade head

# Test connectivity
curl http://localhost:8000/health          # Backend health
curl http://localhost:5173/api/health      # Frontend proxy
```

## 🚀 Deployment

### Production Checklist
- [ ] Environment variables configured (use `env.production.example`)
- [ ] Strong SECRET_KEY generated (32+ characters)
- [ ] Secure admin password set
- [ ] Database migrations applied
- [ ] Frontend built for production (`npm run build`)
- [ ] Email provider configured (Resend/Gmail)
- [ ] Domain configuration set up
- [ ] Security settings reviewed

### Quick Deployment Commands
```bash
# Environment setup
cp env.production.example .env
# Edit .env with production values

# Generate secure secret key
python -c "import secrets; print('SECRET_KEY=' + secrets.token_urlsafe(32))"

# Backend Docker build
cd backend && docker build -t fastapi-backend .

# Frontend production build
cd frontend && npm run build

# Apply migrations
cd backend && uv run alembic upgrade head
```

### Environment Configuration Examples

#### Local Development
```bash
ENVIRONMENT=local
DATABASE_TYPE=sqlite
BACKEND_HOST=localhost
BACKEND_PORT=8000
FRONTEND_HOST=localhost
FRONTEND_PORT=5173
EMAIL_PROVIDER=mailhog
```

#### Production Same-Domain Deployment
```bash
ENVIRONMENT=prod
DATABASE_TYPE=postgresql
DOMAIN=yourdomain.com
BACKEND_PATH=/api
FRONTEND_PATH=
USE_SSL=true
EMAIL_PROVIDER=resend
```

## 🐛 Troubleshooting

### Common Backend Issues

**Database Connection Failed**
```bash
# Check if PostgreSQL is running
docker ps | grep postgres
docker exec -it local-postgres pg_isready -U postgres

# Check SQLite permissions
mkdir -p ./data && chmod 755 ./data
```

**Migration Errors**
```bash
# Reset migrations (development only)
rm migrations/versions/*.py
uv run alembic stamp head
uv run alembic revision --autogenerate -m "Initial migration"
uv run alembic upgrade head
```

**Import/Module Errors**
```bash
# Reinstall dependencies
rm -rf .venv
uv sync
```

### Common Frontend Issues

**API Connection Failed**
```bash
# Check backend is running
curl http://localhost:8000/health

# Verify Vite proxy configuration in vite.config.ts
# Ensure proxy target matches backend port
```

**Build Errors**
```bash
# Clear TypeScript cache
rm -rf node_modules/.cache
npm run type-check

# Clear and reinstall
rm -rf node_modules package-lock.json
npm install
```

**Authentication Issues**
```bash
# Clear browser storage
# Open Dev Tools → Application → Local Storage → Clear

# Check JWT token format in localStorage
# Verify backend auth endpoints are working
```

### Performance Issues

**Backend Slow**
```bash
# Check database connections
# Review SQLAlchemy query performance
# Enable debug logging: --log-level debug
```

**Frontend Slow**
```bash
# Clear Vite cache
rm -rf .vite node_modules/.vite
npm run dev

# Check bundle size
npm run build && ls -la dist/
```

## 🤝 Contributing

We welcome contributions! Here's how to get started:

### Development Setup for Contributors
1. Fork the repository and clone your fork
2. Set up the development environment following the [Quick Start](#-quick-start)
3. Create a feature branch: `git checkout -b feature/your-feature-name`
4. Make your changes following our guidelines below

### Coding Standards

#### Backend Standards
- **Python Style**: Follow PEP 8 formatting
- **Type Hints**: Use Python type annotations consistently
- **Docstrings**: Use Google style docstrings for functions and classes
- **Testing**: Write tests for new features and bug fixes
- **Services**: Follow the existing service-oriented architecture

#### Frontend Standards
- **TypeScript**: Use strict TypeScript for all new code
- **Components**: Follow existing component patterns and structure
- **Styling**: Use Tailwind CSS classes instead of custom CSS
- **Testing**: Add type checking for new components

### Pull Request Process
1. **Update Documentation**: Update relevant README sections for new features
2. **Run Tests**: Ensure all tests pass
   ```bash
   cd backend && uv run pytest
   cd frontend && npm run type-check && npm run lint
   ```
3. **Database Changes**: Create migrations for schema changes
   ```bash
   cd backend && uv run alembic revision --autogenerate -m "Description"
   ```
4. **Commit Messages**: Use clear, descriptive commit messages
5. **Pull Request**: Submit PR with description of changes and any breaking changes

### Development Checklist
- [ ] All tests pass (`uv run pytest` and `npm run type-check`)
- [ ] No linting errors (`npm run lint`)
- [ ] Database migrations created if schema changed
- [ ] Documentation updated if new features added
- [ ] Environment variables documented if added
- [ ] Security considerations reviewed

### Project Structure Guidelines
- **Backend Services**: Place new services under `src/backend/services/`
- **Frontend Components**: Organize in `src/components/` with clear naming
- **Tests**: Mirror source structure in `tests/` directory
- **Documentation**: Update this README for user-facing changes

### Getting Help
- 📖 Check this README for setup and development info
- 🔍 Search existing issues before creating new ones
- 💬 Use GitHub discussions for questions
- 🐛 Report bugs with detailed reproduction steps

---

## 📊 Project Stats

- **Backend**: FastAPI + SQLAlchemy + FastAPI-Users
- **Frontend**: React + TypeScript + Vite + Tailwind
- **Database**: SQLite (dev) / PostgreSQL (prod)
- **Authentication**: JWT with email verification
- **Testing**: Pytest (backend) + TypeScript (frontend)
- **Container**: Docker + Docker Compose ready

---

**🎉 Happy coding!** This template provides a solid foundation for building modern web applications with FastAPI and React.

> **📝 Documentation**: This README contains all essential information for human developers. AI agents should refer to files in the `agent/` directory for technical implementation details.