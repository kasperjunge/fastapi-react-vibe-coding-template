# FastAPI-React Vibe Coding Template

A modern, full-stack web application template featuring FastAPI backend with database independence and React frontend with complete authentication system.

## 📚 Quick Navigation

- [🚀 Features](#-features)
- [📁 Project Structure](#-project-structure) 
- [⚡ Quick Start](#-quick-start)
- [🛠️ Detailed Setup](#️-detailed-setup)
- [🗄️ Database Options](#️-database-options)
- [🧪 Testing](#-testing)
- [🐳 Docker Development](#-docker-development)
- [📖 Documentation](#-documentation)
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

### Environment & DevOps ([📖 Environment Setup Guide](ENVIRONMENT_SETUP.md))
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
│   ├── 📄 README.md             # Backend documentation
│   ├── 📄 CONTRIBUTING.md       # Contribution guidelines
│   └── 📄 Dockerfile            # Backend container
├── 📁 frontend/                  # React frontend with auth components
│   ├── 📁 src/                   # Frontend source code
│   │   ├── 📁 components/        # React components (auth, UI)
│   │   ├── 📁 contexts/          # React contexts (Auth)
│   │   └── 📁 lib/               # Utilities (API client)
│   ├── 📄 README.md             # Frontend documentation
│   └── 📄 package.json          # Node.js dependencies
├── 📁 agent/                     # AI assistant documentation
│   ├── 📄 CURRENT_TASK.md       # Current project status
│   ├── 📄 CODEBASE.md           # Technical documentation
│   └── 📄 SCRATCHPAD.md         # Development insights
├── 📄 docker-compose.yml         # Multi-service setup
├── 📄 ENVIRONMENT_SETUP.md       # Comprehensive environment guide
├── 📄 NOTES.md                   # Development notes & quick reference
├── 📄 env.example                # Environment template
├── 📄 env.local.example          # Local development template
├── 📄 env.production.example     # Production template
└── 📄 README.md                  # This file
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

> **💡 Tip**: For detailed setup options, see the [🛠️ Detailed Setup](#️-detailed-setup) section below.

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
# Configure production settings
```

> **📖 For comprehensive environment configuration**: See [ENVIRONMENT_SETUP.md](ENVIRONMENT_SETUP.md)

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

> **📖 Backend details**: See [backend/README.md](backend/README.md)

### 3. Frontend Setup

```bash
cd frontend
npm install                    # Install dependencies
npm run dev                    # Start the development server
```

**Available at:**
- 🌐 Frontend: `http://localhost:5173`

> **📖 Frontend details**: See [frontend/README.md](frontend/README.md)

### 4. Email Testing (Optional)

For email verification testing:
```bash
docker run -d -p 1025:1025 -p 8025:8025 mailhog/mailhog
# Access email interface at http://localhost:8025
```

> **📖 Development commands**: See [NOTES.md](NOTES.md) for more commands and troubleshooting

## 🗄️ Database Options

This template supports seamless switching between databases:

### SQLite (Default)
- ✅ **Pros**: No external dependencies, fast setup, perfect for development
- ⚠️ **Cons**: Single-user, not suitable for production with multiple users
- 🎯 **Use cases**: Development, testing, small single-user applications

### PostgreSQL
- ✅ **Pros**: Production-ready, multi-user, advanced features, excellent performance
- ⚠️ **Cons**: Requires external service, more complex setup
- 🎯 **Use cases**: Production, development with production-like environment

### Switching Databases
```bash
# 1. Update DATABASE_TYPE in your .env file
# 2. Configure the appropriate database settings
# 3. Run migrations
cd backend && uv run alembic upgrade head
# 4. Restart the application
```

> **📖 Database configuration examples**: See [agent/DATABASE_CONFIG_EXAMPLES.md](agent/DATABASE_CONFIG_EXAMPLES.md)

## 🧪 Testing

### Backend Tests
```bash
cd backend
uv run pytest                  # Run all tests
uv run pytest -v              # Verbose output
uv run pytest --cov           # With coverage report
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
```

## 🐳 Docker Development

**Run the entire stack with Docker Compose:**
```bash
docker-compose up -d
```

**This starts:**
- 🗄️ PostgreSQL database (if using PostgreSQL)
- 🚀 Backend API server
- ⚛️ Frontend development server

**Individual services:**
```bash
docker-compose up -d db        # Database only
docker-compose up -d backend   # Backend only
docker-compose up -d frontend  # Frontend only
```

## 📖 Documentation

### For Developers
- 📖 **[Backend Documentation](backend/README.md)** - FastAPI backend details
- 📖 **[Frontend Documentation](frontend/README.md)** - React frontend details
- 📖 **[Environment Setup Guide](ENVIRONMENT_SETUP.md)** - Comprehensive configuration guide
- 📖 **[Development Notes](NOTES.md)** - Quick reference and troubleshooting
- 📖 **[Contributing Guidelines](backend/CONTRIBUTING.md)** - How to contribute

### For AI Agents
- 🤖 **[Current Task](agent/CURRENT_TASK.md)** - Project status and ongoing work
- 🤖 **[Codebase Documentation](agent/CODEBASE.md)** - Technical implementation details
- 🤖 **[Scratchpad](agent/SCRATCHPAD.md)** - Development insights and notes

### Configuration References
- ⚙️ **[Database Examples](agent/DATABASE_CONFIG_EXAMPLES.md)** - Database setup examples
- ⚙️ **[Environment Analysis](agent/ENV_ANALYSIS_AND_RECOMMENDATIONS.md)** - Environment recommendations

## 🔧 Adding New Features

### Backend Service
1. Create a new service directory in `backend/src/backend/services/`
2. Implement SQLAlchemy models, Pydantic schemas, business logic, and routes
3. Register the router in `backend/src/backend/app.py`
4. Add tests in `backend/tests/services/`

> **📖 Detailed guide**: See [backend/README.md](backend/README.md#adding-a-new-service)

### Frontend Components
1. Create components in `frontend/src/components/`
2. Add routes in `frontend/src/App.tsx`
3. Use the API client from `frontend/src/lib/api.ts`
4. Follow authentication patterns from existing auth components

> **📖 Detailed guide**: See [frontend/README.md](frontend/README.md#adding-new-features)

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Read the guidelines**: [backend/CONTRIBUTING.md](backend/CONTRIBUTING.md)
2. **Fork the repository** and create a feature branch
3. **Follow the coding standards** and add tests
4. **Update documentation** if needed
5. **Submit a pull request** with a clear description

### Development Checklist
- [ ] All tests pass (`uv run pytest` and `npm run type-check`)
- [ ] No linting errors (`npm run lint`)
- [ ] Database migrations created if schema changed
- [ ] Documentation updated if new features added

## 🚀 Deployment

### Production Checklist
- [ ] Environment variables configured (use `env.production.example`)
- [ ] Database migrations applied
- [ ] Frontend built for production (`npm run build`)
- [ ] Security settings reviewed
- [ ] Email functionality verified

### Quick Deployment Commands
```bash
# Backend Docker build
cd backend && docker build -t fastapi-backend .

# Frontend production build
cd frontend && npm run build

# Environment setup
cp env.production.example .env  # Then configure
```

## 📊 Project Stats

- **Backend**: FastAPI + SQLAlchemy + FastAPI-Users
- **Frontend**: React + TypeScript + Vite + Tailwind
- **Database**: SQLite (dev) / PostgreSQL (prod)
- **Authentication**: JWT with email verification
- **Testing**: Pytest (backend) + TypeScript (frontend)
- **Container**: Docker + Docker Compose ready

## 📞 Support

- 📖 **Documentation**: Check the relevant README files above
- 🐛 **Issues**: Use GitHub issues for bug reports
- 💡 **Features**: Use GitHub issues for feature requests
- 🤝 **Contributing**: See [CONTRIBUTING.md](backend/CONTRIBUTING.md)

---

**🎉 Happy coding!** This template provides a solid foundation for building modern web applications with FastAPI and React.