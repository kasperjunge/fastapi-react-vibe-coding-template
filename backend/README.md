# FastAPI Backend Template

A modern, production-ready backend template built with FastAPI, SQLAlchemy, and Pydantic.

## Features

- **FastAPI**: High-performance, easy-to-learn, fast to code, ready for production
- **SQLAlchemy**: Async SQL database operations with PostgreSQL
- **FastAPI-Users**: Complete authentication system with user management
- **Alembic**: Database migrations and schema management
- **Pydantic**: Data validation and settings management using Python type hints
- **Service-oriented architecture**: Modular structure for maintainability and scalability
- **Docker support**: Ready for containerized deployment

## Project Structure

```
backend/
├── src/                    # Source code directory
│   └── backend/            # Main application package
│       ├── app.py          # FastAPI app setup and configuration
│       ├── db.py           # SQLAlchemy database connection and session management
│       ├── settings.py     # Pydantic settings and configuration
│       ├── main.py         # Application entry point
│       └── services/       # Service modules (feature-based)
│           ├── auth/       # Authentication service (FastAPI-Users)
│           ├── users/      # User management
│           │   ├── models.py     # SQLAlchemy User model
│           │   └── ...
│           └── example_service/  # Example service module
│               ├── models.py     # SQLAlchemy models
│               ├── schemas.py    # Pydantic schemas for request/response validation
│               ├── routes.py     # API route definitions
│               └── service.py    # Business logic implementation
├── tests/                  # Test directory
│   ├── test_app.py         # Tests for app.py
│   ├── test_db.py          # Tests for db.py
│   ├── test_main.py        # Tests for main.py
│   ├── test_settings.py    # Tests for settings.py
│   └── services/           # Tests for service modules
│       ├── auth/           # Tests for auth service
│       ├── users/          # Tests for users service
│       └── example_service/ # Tests for example service
│           ├── test_models.py    # Tests for models.py
│           ├── test_routes.py    # Tests for routes.py
│           ├── test_schemas.py   # Tests for schemas.py
│           └── test_service.py   # Tests for service.py
├── migrations/             # Alembic migration files
├── alembic.ini            # Alembic configuration
├── pyproject.toml          # Project metadata and dependencies (uv)
├── uv.lock                 # Lock file for dependencies
├── .python-version         # Python version specification
├── Dockerfile              # Docker container definition 
└── README.md               # Project documentation
```

## Getting Started

### Local Development

Install environment:
```bash
uv sync
```

Set up environment variables (create `.env` in project root):
```bash
# Example .env file
ENVIRONMENT=dev
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=secret
BACKEND_HOST=localhost
BACKEND_PORT=8000
SECRET_KEY=your-secret-key-here
# ... other variables from settings.py
```

Set up the database:
```bash
# Using Docker Compose (from project root)
docker-compose up -d db

# Or manually
docker run --name local-postgres \
  -e POSTGRES_DB=db \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=secret \
  -p 5432:5432 \
  -v pgdata:/var/lib/postgresql/data \
  -d postgres
```

Run migrations:
```bash
uv run alembic upgrade head
```

Run the backend:
```bash
uv run backend
```

The API will be available at:
- Main API: `http://localhost:8000`
- Interactive docs: `http://localhost:8000/docs`
- Alternative docs: `http://localhost:8000/redoc`

### Testing

Run all tests:
```bash
uv run pytest
```

Run tests with coverage:
```bash
uv run pytest --cov=backend
```

## Adding a New Service

1. Create a new directory in `src/backend/services/`
2. Implement `models.py` using SQLAlchemy with the `Base` from `backend.db`
3. Create Pydantic schemas in `schemas.py` for request/response validation
4. Implement business logic in `service.py`
5. Create API endpoints in `routes.py`
6. Register the router in `src/backend/app.py`
7. Create corresponding test files in `tests/services/your_service/`

### Example Service Structure

```python
# models.py
from sqlalchemy import Column, Integer, String
from backend.db import Base

class ExampleModel(Base):
    __tablename__ = "example"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

# schemas.py
from pydantic import BaseModel

class ExampleCreate(BaseModel):
    name: str

class ExampleResponse(BaseModel):
    id: int
    name: str

# routes.py
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from backend.db import get_async_session

router = APIRouter(prefix="/example", tags=["example"])

@router.post("/", response_model=ExampleResponse)
async def create_example(
    example: ExampleCreate,
    session: AsyncSession = Depends(get_async_session)
):
    # Implementation here
    pass
```

## Database Migrations

Create a new migration:
```bash
uv run alembic revision --autogenerate -m "Description of changes"
```

Apply migrations:
```bash
uv run alembic upgrade head
```

Downgrade migrations:
```bash
uv run alembic downgrade -1
```

## Authentication

This template uses FastAPI-Users for authentication. The user model and authentication routes are set up in the `services/auth/` and `services/users/` directories.

## Contributing

Please read `CONTRIBUTING.md` for details on our code of conduct and the process for submitting pull requests.
