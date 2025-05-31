# Development Notes & Quick Reference

This file contains useful commands, troubleshooting tips, and development notes for the FastAPI-React template.

## 🐳 Database Setup

### PostgreSQL with Docker

```bash
# Run Local PostgreSQL in Docker Container
docker run --name local-postgres \
  -e POSTGRES_DB=db \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=secret \
  -p 5432:5432 \
  -v pgdata:/var/lib/postgresql/data \
  -d postgres

# Access PostgreSQL Database
docker exec -it local-postgres psql -U postgres -d db

# Stop and remove container
docker stop local-postgres
docker rm local-postgres

# Remove volume (destroys data)
docker volume rm pgdata
```

### Using Docker Compose
```bash
# Start database only
docker-compose up -d db

# Start all services
docker-compose up -d

# Stop all services
docker-compose down

# Stop and remove volumes
docker-compose down -v
```

## 🔧 Backend Development

### Environment & Dependencies
```bash
# Install/update dependencies
cd backend
uv sync

# Add new dependency
uv add package-name

# Install development dependency
uv add --dev package-name

# Run backend server
uv run backend

# Run with auto-reload (for development)
uv run uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

### Database Migrations
```bash
cd backend

# Create new migration
uv run alembic revision --autogenerate -m "Description of changes"

# Apply migrations
uv run alembic upgrade head

# Rollback one migration
uv run alembic downgrade -1

# View migration history
uv run alembic history

# Current migration info
uv run alembic current
```

### Testing
```bash
cd backend

# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=backend --cov-report=html

# Run specific test file
uv run pytest tests/test_auth.py

# Run with verbose output
uv run pytest -v

# Run and stop on first failure
uv run pytest -x
```

## ⚛️ Frontend Development

### Dependencies & Development
```bash
cd frontend

# Install dependencies
npm install

# Add new dependency
npm install package-name

# Add development dependency
npm install --save-dev package-name

# Start development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview

# Type checking
npm run type-check

# Linting
npm run lint
```

### Troubleshooting Frontend
```bash
# Clear node_modules and reinstall
rm -rf node_modules package-lock.json
npm install

# Clear Vite cache
rm -rf .vite node_modules/.vite
npm run dev

# Check TypeScript compilation
npm run type-check

# Fix linting issues
npm run lint -- --fix
```

## 📧 Email Testing

### MailHog (Development)
```bash
# Start MailHog container
docker run -d -p 1025:1025 -p 8025:8025 mailhog/mailhog

# Access web interface
open http://localhost:8025

# Environment variables for MailHog
EMAIL_PROVIDER=mailhog
MAIL_PORT=1025
MAIL_SERVER=localhost
```

### Gmail SMTP (Production)
```bash
# Environment variables for Gmail
EMAIL_PROVIDER=gmail
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_STARTTLS=true
```

## 🔍 Debugging & Monitoring

### Backend Debugging
```bash
# Check API documentation
open http://localhost:8000/docs

# View logs with more detail
uv run uvicorn backend.main:app --reload --log-level debug

# Test API endpoints
curl -X GET http://localhost:8000/health
curl -X POST http://localhost:8000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"password"}'
```

### Database Debugging
```bash
# Connect to SQLite database
sqlite3 ./data/app.db
.tables
.schema users

# PostgreSQL queries
docker exec -it local-postgres psql -U postgres -d db -c "SELECT * FROM users;"
```

### Frontend Debugging
```bash
# Check API connectivity
curl http://localhost:5173/api/health

# Inspect Vite proxy configuration
# Check vite.config.ts for proxy settings

# Debug authentication
# Check browser localStorage for 'token' key
# Check browser Network tab for API calls
```

## 🚀 Deployment Commands

### Production Build
```bash
# Build backend Docker image
cd backend
docker build -t fastapi-backend .

# Build frontend
cd frontend
npm run build

# Test production build locally
cd frontend
npm run preview
```

### Environment Setup
```bash
# Copy environment templates
cp env.local.example .env        # For local development
cp env.production.example .env   # For production

# Generate secure secret key
python -c "import secrets; print('SECRET_KEY=' + secrets.token_urlsafe(32))"
```

## 🔧 Useful Development Commands

### Code Quality
```bash
# Backend code formatting (if using black)
cd backend
uv run black src/

# Frontend code formatting (if using prettier)
cd frontend
npx prettier --write src/

# Check for unused dependencies
cd backend
uv run pip-audit  # Security audit

cd frontend
npm audit  # Security audit
npx depcheck  # Unused dependencies
```

### Project Management
```bash
# Update all Python dependencies
cd backend
uv sync --upgrade

# Update all Node.js dependencies
cd frontend
npm update

# Check for outdated packages
cd frontend
npm outdated
```

## 🐛 Common Issues & Solutions

### Backend Issues

**1. Database Connection Failed**
```bash
# Check if PostgreSQL is running
docker ps | grep postgres

# Test connection
docker exec -it local-postgres pg_isready -U postgres
```

**2. Migration Errors**
```bash
# Reset migrations (development only)
cd backend
rm migrations/versions/*.py
uv run alembic stamp head
uv run alembic revision --autogenerate -m "Initial migration"
uv run alembic upgrade head
```

**3. Permission Errors (SQLite)**
```bash
# Fix SQLite permissions
mkdir -p ./data
chmod 755 ./data
```

### Frontend Issues

**1. API Connection Failed**
```bash
# Check if backend is running
curl http://localhost:8000/health

# Check Vite proxy configuration
# Verify vite.config.ts proxy settings match backend port
```

**2. Build Errors**
```bash
# Clear TypeScript cache
rm -rf frontend/node_modules/.cache
npm run type-check
```

**3. Authentication Issues**
```bash
# Clear authentication state
# Open browser dev tools → Application → Local Storage → Clear
```

## 📋 Development Checklist

### Before Committing
- [ ] All tests pass (`uv run pytest` and `npm test`)
- [ ] No TypeScript errors (`npm run type-check`)
- [ ] No linting errors (`npm run lint`)
- [ ] Database migrations created if schema changed
- [ ] Environment variables documented if added
- [ ] README updated if new features added

### Before Deployment
- [ ] Production environment variables configured
- [ ] Database migrations applied
- [ ] Frontend built for production
- [ ] API endpoints tested
- [ ] Email functionality verified
- [ ] Security settings reviewed

## 📚 Quick Links

- **Backend API Docs**: http://localhost:8000/docs
- **Frontend Dev Server**: http://localhost:5173
- **MailHog Interface**: http://localhost:8025
- **PostgreSQL Admin**: Use pgAdmin or similar tool on localhost:5432

## 📝 TODO Items

### High Priority
- [ ] Add comprehensive error handling and user feedback
- [ ] Implement rate limiting for authentication endpoints
- [ ] Add logging and monitoring capabilities
- [ ] Create deployment automation scripts

### Medium Priority
- [ ] Add password reset functionality
- [ ] Implement user profile management
- [ ] Add API versioning
- [ ] Create comprehensive integration tests

### Low Priority
- [ ] Add social authentication (Google, GitHub)
- [ ] Implement real-time features with WebSockets
- [ ] Add API rate limiting dashboard
- [ ] Create development environment setup script

---

**Last Updated**: Current documentation review
**Maintainer**: See CONTRIBUTING.md for contribution guidelines
