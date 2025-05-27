# FastAPI-React Vibe Coding Template

A modern, full-stack web application template featuring FastAPI backend with SQLAlchemy and React frontend.

## 🚀 Features

### Backend
- **FastAPI**: High-performance, easy-to-learn, fast to code, ready for production
- **SQLAlchemy**: Async SQL database operations with PostgreSQL
- **FastAPI-Users**: Complete authentication system with user management
- **Alembic**: Database migrations
- **Pydantic**: Data validation and settings management
- **Service-oriented architecture**: Modular structure for maintainability and scalability
- **Docker support**: Ready for containerized deployment

### Frontend
- **React**: Modern frontend framework
- **Vite**: Fast build tool and development server

## 📁 Project Structure

```
fastapi-react-vibe-coding-template/
├── backend/                    # FastAPI backend
│   ├── src/backend/           # Source code
│   │   ├── services/          # Feature-based services
│   │   │   ├── auth/          # Authentication (FastAPI-Users)
│   │   │   ├── users/         # User management
│   │   │   └── example_service/ # Example service template
│   │   ├── app.py             # FastAPI app setup
│   │   ├── db.py              # SQLAlchemy configuration
│   │   ├── main.py            # Application entry point
│   │   └── settings.py        # Configuration settings
│   ├── migrations/            # Alembic database migrations
│   ├── tests/                 # Test suite
│   ├── pyproject.toml         # Python dependencies (uv)
│   └── Dockerfile             # Backend container
├── frontend/                  # React frontend
├── docker-compose.yml         # Multi-service setup
├── NOTES.md                   # Development notes
└── README.md                  # This file
```

## 🛠️ Getting Started

### Prerequisites
- Python 3.12+
- Node.js 18+
- Docker (optional, for database)
- [uv](https://docs.astral.sh/uv/) (Python package manager)

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd fastapi-react-vibe-coding-template
```

### 2. Set Up Environment Variables
Create a `.env` file in the project root:

```bash
# Environment
ENVIRONMENT=dev

# Database
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
```

### 3. Set Up the Database
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

## 🧪 Testing

### Backend Tests
```bash
cd backend
uv run pytest
```

## 🐳 Docker Development

Run the entire stack with Docker Compose:
```bash
docker-compose up -d
```

## 📝 Development Notes

- Database access: `docker exec -it local-postgres psql -U postgres -d db`
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

## 📋 Todo
- [ ] Email verification + password reset
- [ ] Enhanced logging
- [ ] Admin dashboard
- [ ] API rate limiting
- [ ] Frontend state management
- [ ] E2E testing setup

## 🤝 Contributing

Please read `backend/CONTRIBUTING.md` for details on our code of conduct and the process for submitting pull requests.

## 📄 License

This project is licensed under the MIT License.