# FastAPI-React Vibe Coding Template

A modern, full-stack web application template featuring FastAPI backend with database independence and React frontend.

## 🚀 Features

### Backend
- **FastAPI**: High-performance, easy-to-learn, fast to code, ready for production
- **Database Independence**: Support for both SQLite (development) and PostgreSQL (production)
- **SQLAlchemy**: Async SQL database operations with automatic driver selection
- **FastAPI-Users**: Complete authentication system with user management
- **Email Verification**: Complete email verification system with multiple providers
- **Alembic**: Database migrations that work with both database types
- **Pydantic**: Data validation and settings management
- **Service-oriented architecture**: Modular structure for maintainability and scalability
- **Docker support**: Ready for containerized deployment

### Frontend
- **React**: Modern frontend framework with TypeScript
- **Authentication Flow**: Complete registration, verification, and login system
- **Vite**: Fast build tool and development server
- **Tailwind CSS**: Utility-first CSS framework

## 📁 Project Structure

```
fastapi-react-vibe-coding-template/
├── backend/                    # FastAPI backend
│   ├── src/backend/           # Source code
│   │   ├── services/          # Feature-based services
│   │   │   ├── auth/          # Authentication (FastAPI-Users)
│   │   │   ├── users/         # User management
│   │   │   ├── email/         # Email verification service
│   │   │   └── example_service/ # Example service template
│   │   ├── app.py             # FastAPI app setup
│   │   ├── db.py              # Database configuration (SQLite/PostgreSQL)
│   │   ├── main.py            # Application entry point
│   │   └── settings.py        # Configuration settings
│   ├── migrations/            # Alembic database migrations
│   ├── tests/                 # Comprehensive test suite
│   ├── pyproject.toml         # Python dependencies (uv)
│   └── Dockerfile             # Backend container
├── frontend/                  # React frontend with auth components
├── agent/                     # AI assistant documentation
├── docker-compose.yml         # Multi-service setup
├── NOTES.md                   # Development notes
└── README.md                  # This file
```

## 🛠️ Getting Started

### Prerequisites
- Python 3.12+
- Node.js 18+
- Docker (optional, for PostgreSQL)
- [uv](https://docs.astral.sh/uv/) (Python package manager)

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd fastapi-react-vibe-coding-template
```

### 2. Set Up Environment Variables
Create a `.env` file in the project root. Choose your database configuration:

#### Option A: SQLite (Default - No external dependencies)
```bash
# Environment
ENVIRONMENT=dev

# Database (SQLite - default for development)
DATABASE_TYPE=sqlite
SQLITE_DB_PATH=./data/app.db

# Backend
BACKEND_HOST=localhost
BACKEND_PORT=8000

# Frontend
VITE_API_URL=http://localhost:8000
FRONTEND_PORT=3000

# Admin User
ADMIN_EMAIL=admin@example.com
ADMIN_USERNAME=admin
ADMIN_PASSWORD=admin123
ADMIN_FIRST_NAME=Admin
ADMIN_LAST_NAME=User

# Security
SECRET_KEY=your-secret-key-here

# Email (MailHog for development)
EMAIL_PROVIDER=mailhog
VERIFICATION_TOKEN_EXPIRE_HOURS=24
```

#### Option B: PostgreSQL (Production-like setup)
```bash
# Environment
ENVIRONMENT=dev

# Database (PostgreSQL)
DATABASE_TYPE=postgresql
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=secret

# Backend
BACKEND_HOST=localhost
BACKEND_PORT=8000

# Frontend
VITE_API_URL=http://localhost:8000
FRONTEND_PORT=3000

# Admin User
ADMIN_EMAIL=admin@example.com
ADMIN_USERNAME=admin
ADMIN_PASSWORD=admin123
ADMIN_FIRST_NAME=Admin
ADMIN_LAST_NAME=User

# Security
SECRET_KEY=your-secret-key-here

# Email (MailHog for development)
EMAIL_PROVIDER=mailhog
VERIFICATION_TOKEN_EXPIRE_HOURS=24
```

> 📋 **See `agent/DATABASE_CONFIG_EXAMPLES.md` for more configuration examples and detailed setup instructions.**

### 3. Set Up the Database

#### For SQLite (Default)
No additional setup required! The database file will be created automatically.

#### For PostgreSQL
Using Docker Compose (recommended):
```bash
docker-compose up -d db
```

Or manually with Docker:
```bash
docker run --name local-postgres \
  -e POSTGRES_DB=db \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=secret \
  -p 5432:5432 \
  -v pgdata:/var/lib/postgresql/data \
  -d postgres
```

### 4. Set Up the Backend
```bash
cd backend
uv sync                        # Install dependencies
uv run alembic upgrade head    # Run database migrations
uv run backend                 # Start the backend server
```

The API will be available at `http://localhost:8000`
- API Documentation: `http://localhost:8000/docs`
- Alternative docs: `http://localhost:8000/redoc`

### 5. Set Up the Frontend
```bash
cd frontend
npm install                    # Install dependencies
npm run dev                    # Start the development server
```

The frontend will be available at `http://localhost:3000`

### 6. Set Up Email Testing (Optional)
For email verification testing, start MailHog:
```bash
docker run -d -p 1025:1025 -p 8025:8025 mailhog/mailhog
```
Access the email interface at `http://localhost:8025`

## 🗄️ Database Options

### SQLite (Default)
- **Pros**: No external dependencies, fast setup, perfect for development
- **Cons**: Single-user, not suitable for production with multiple users
- **Use cases**: Development, testing, small single-user applications

### PostgreSQL
- **Pros**: Production-ready, multi-user, advanced features, excellent performance
- **Cons**: Requires external service, more complex setup
- **Use cases**: Production, development with production-like environment

### Switching Databases
You can easily switch between databases by changing the `DATABASE_TYPE` environment variable:
1. Update `DATABASE_TYPE` in your `.env` file
2. Configure the appropriate database settings
3. Run migrations: `uv run alembic upgrade head`
4. Restart the application

## 🧪 Testing

### Backend Tests
```bash
cd backend
uv run pytest                  # Run all tests
uv run pytest -v              # Verbose output
uv run pytest --cov           # With coverage report
```

The test suite includes:
- User service tests (registration, verification, authentication)
- Email service tests (template rendering, sending)
- API endpoint tests (auth flows, protected routes)
- Authentication flow tests (JWT, verification)

## 🐳 Docker Development

Run the entire stack with Docker Compose:
```bash
docker-compose up -d
```

This starts:
- PostgreSQL database (if using PostgreSQL)
- Backend API server
- Frontend development server

## 📝 Development Notes

- **SQLite database**: Located at `./data/app.db` (created automatically)
- **PostgreSQL access**: `docker exec -it local-postgres psql -U postgres -d db`
- **Email testing**: MailHog web interface at `http://localhost:8025`
- See `NOTES.md` for additional development commands
- Check `backend/CONTRIBUTING.md` for detailed contribution guidelines

## 🔧 Adding New Features

### Backend Service
1. Create a new service directory in `backend/src/backend/services/`
2. Implement SQLAlchemy models, Pydantic schemas, business logic, and routes
3. Register the router in `backend/src/backend/app.py`
4. Add tests in `backend/tests/services/`

### Frontend Components
1. Add components in the appropriate frontend directory
2. Follow the existing component structure and patterns
3. Use the auth context for protected routes

## ✅ Completed Features
- ✅ **Database Independence**: SQLite and PostgreSQL support
- ✅ **Email Verification**: Complete verification system with multiple providers
- ✅ **Authentication Flow**: Registration, verification, login with JWT
- ✅ **Comprehensive Testing**: Backend test suite with excellent coverage
- ✅ **Service Architecture**: Modular, maintainable code structure

## 📋 Todo
- [ ] Frontend testing setup (Jest, React Testing Library)
- [ ] Enhanced logging and monitoring
- [ ] Admin dashboard
- [ ] API rate limiting
- [ ] E2E testing setup
- [ ] CI/CD pipeline

## 🤝 Contributing

Please read `backend/CONTRIBUTING.md` for details on our code of conduct and the process for submitting pull requests.

## 📄 License

This project is licensed under the MIT License.