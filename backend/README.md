# FastAPI Backend

A modern, production-ready backend template built with FastAPI, SQLAlchemy, and Pydantic with database independence support.

## 📚 Quick Navigation

- [🚀 Features](#-features)
- [📁 Project Structure](#-project-structure)
- [🛠️ Getting Started](#️-getting-started)
- [🗄️ Database Configuration](#️-database-configuration)
- [🔧 Adding New Services](#-adding-new-services)
- [🧪 Testing](#-testing)
- [🤝 Contributing](#-contributing)

## 🚀 Features

- **FastAPI**: High-performance, easy-to-learn, fast to code, ready for production
- **Database Independence**: Support for both SQLite (development) and PostgreSQL (production)
- **SQLAlchemy**: Async SQL database operations with automatic driver selection
- **FastAPI-Users**: Complete authentication system with user management
- **Email Verification**: Multi-provider email system (MailHog, Gmail, Resend)
- **Alembic**: Database migrations that work with both database types
- **Pydantic**: Data validation and settings management using Python type hints
- **Service-oriented architecture**: Modular structure for maintainability and scalability
- **Docker support**: Ready for containerized deployment

## 📁 Project Structure

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
│           │   ├── service.py    # UserManager with email verification
│           │   ├── routes.py     # API route definitions
│           │   ├── schemas.py    # Pydantic schemas
│           │   └── dependencies.py # Dependency injection
│           ├── email/      # Email service
│           │   ├── service.py    # EmailService with multi-provider support
│           │   └── templates/    # Email templates (HTML)
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
└── README.md               # This file
```

## 🛠️ Getting Started

### Prerequisites
- Python 3.12+
- [uv](https://docs.astral.sh/uv/) (Python package manager)
- Docker (optional, for PostgreSQL)

### Local Development

1. **Install environment:**
   ```bash
   uv sync
   ```

2. **Set up environment variables** (create `.env` in project root):
   ```bash
   # Example .env file
   ENVIRONMENT=local
   DATABASE_TYPE=sqlite  # or postgresql
   SQLITE_DB_PATH=./data/app.db
   
   # For PostgreSQL
   POSTGRES_HOST=localhost
   POSTGRES_PORT=5432
   POSTGRES_DB=db
   POSTGRES_USER=postgres
   POSTGRES_PASSWORD=secret
   
   BACKEND_HOST=localhost
   BACKEND_PORT=8000
   SECRET_KEY=your-secret-key-here
   
   # Admin user
   ADMIN_EMAIL=admin@example.com
   ADMIN_USERNAME=admin
   ADMIN_PASSWORD=secure-password
   ADMIN_FIRST_NAME=Admin
   ADMIN_LAST_NAME=User
   
   # Email (MailHog for development)
   EMAIL_PROVIDER=mailhog
   MAIL_PORT=1025
   MAIL_SERVER=localhost
   VERIFICATION_TOKEN_EXPIRE_HOURS=24
   ```

3. **Set up the database:**
   
   **For SQLite (default):**
   ```bash
   # No additional setup required - database file created automatically
   ```
   
   **For PostgreSQL:**
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

4. **Run migrations:**
   ```bash
   uv run alembic upgrade head
   ```

5. **Run the backend:**
   ```bash
   uv run backend
   ```

The API will be available at:
- Main API: `http://localhost:8000`
- Interactive docs: `http://localhost:8000/docs`
- Alternative docs: `http://localhost:8000/redoc`

## 🗄️ Database Configuration

### SQLite (Default)
- **Pros**: No external dependencies, fast setup, perfect for development
- **Cons**: Single-user, not suitable for production with multiple users
- **Use cases**: Development, testing, small single-user applications

### PostgreSQL
- **Pros**: Production-ready, multi-user, advanced features, excellent performance
- **Cons**: Requires external service, more complex setup
- **Use cases**: Production, development with production-like environment

### Switching Databases
1. Update `DATABASE_TYPE` in your `.env` file
2. Configure the appropriate database settings
3. Run migrations: `uv run alembic upgrade head`
4. Restart the application

## 🔧 Adding New Services

### 1. Create Service Structure
```bash
mkdir -p src/backend/services/your_service
cd src/backend/services/your_service
```

### 2. Implement Models
```python
# models.py
from sqlalchemy import Column, Integer, String
from backend.db import Base

class YourModel(Base):
    __tablename__ = "your_table"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
```

### 3. Create Schemas
```python
# schemas.py
from pydantic import BaseModel

class YourModelCreate(BaseModel):
    name: str

class YourModelResponse(BaseModel):
    id: int
    name: str
    
    class Config:
        from_attributes = True
```

### 4. Implement Business Logic
```python
# service.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from .models import YourModel
from .schemas import YourModelCreate

class YourService:
    @staticmethod
    async def create_item(session: AsyncSession, item: YourModelCreate) -> YourModel:
        db_item = YourModel(**item.dict())
        session.add(db_item)
        await session.commit()
        await session.refresh(db_item)
        return db_item
    
    @staticmethod
    async def get_items(session: AsyncSession) -> list[YourModel]:
        result = await session.execute(select(YourModel))
        return result.scalars().all()
```

### 5. Create API Routes
```python
# routes.py
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from backend.db import get_async_session
from .service import YourService
from .schemas import YourModelCreate, YourModelResponse

router = APIRouter(prefix="/your-service", tags=["your-service"])

@router.post("/", response_model=YourModelResponse)
async def create_item(
    item: YourModelCreate,
    session: AsyncSession = Depends(get_async_session)
):
    return await YourService.create_item(session, item)

@router.get("/", response_model=list[YourModelResponse])
async def get_items(session: AsyncSession = Depends(get_async_session)):
    return await YourService.get_items(session)
```

### 6. Register Router
```python
# In src/backend/app.py
from backend.services.your_service.routes import router as your_service_router

app.include_router(your_service_router, prefix="/api")
```

### 7. Create Migration
```bash
uv run alembic revision --autogenerate -m "Add your_service table"
uv run alembic upgrade head
```

### 8. Add Tests
```python
# tests/services/your_service/test_service.py
import pytest
from sqlalchemy.ext.asyncio import AsyncSession
from backend.services.your_service.service import YourService
from backend.services.your_service.schemas import YourModelCreate

@pytest.mark.asyncio
async def test_create_item(async_session: AsyncSession):
    item_data = YourModelCreate(name="Test Item")
    item = await YourService.create_item(async_session, item_data)
    assert item.name == "Test Item"
    assert item.id is not None
```

## 🧪 Testing

### Run Tests
```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=backend --cov-report=html

# Run specific test file
uv run pytest tests/services/users/test_service.py

# Run with verbose output
uv run pytest -v

# Stop on first failure
uv run pytest -x
```

### Test Structure
- Tests mirror the `src/backend` structure
- Use `pytest` fixtures for database setup
- Async tests for database operations
- Mock external services (email providers)

### Writing Tests
```python
import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

@pytest.mark.asyncio
async def test_api_endpoint(async_client: AsyncClient):
    response = await async_client.post("/api/your-service/", json={"name": "test"})
    assert response.status_code == 200
    assert response.json()["name"] == "test"

@pytest.mark.asyncio
async def test_service_method(async_session: AsyncSession):
    # Test business logic directly
    result = await YourService.some_method(async_session, data)
    assert result is not None
```

## 🤝 Contributing

We welcome contributions to improve the backend! Please follow these guidelines:

### Development Workflow

1. **Fork the repository** and clone your fork:
   ```bash
   git clone https://github.com/your-username/backend.git
   cd backend
   ```

2. **Install dependencies** in a Python 3.12+ environment:
   ```bash
   uv sync
   ```

3. **Set up environment variables** (create `.env` in project root):
   ```bash
   # Copy from the example above and customize
   ```

4. **Set up the database** and run migrations:
   ```bash
   # For PostgreSQL
   docker-compose up -d db
   
   # Run migrations
   uv run alembic upgrade head
   ```

5. **Create a branch** for your work:
   ```bash
   git checkout -b feature/brief-description
   ```

### Coding Guidelines

#### Python Standards
- **Language & Framework**: Python 3.12, FastAPI, SQLAlchemy (async), FastAPI-Users for authentication
- **Formatting**: Follow [PEP 8](https://peps.python.org/pep-0008/)
- **Imports**: Group standard library, third-party, and local imports separately
- **Type Hints**: Use Python type annotations consistently
- **Docstrings**: Use Google style docstrings for modules, classes, functions, and methods:

```python
def add(x: int, y: int) -> int:
    """
    Add two integers.

    Args:
        x: First integer.
        y: Second integer.

    Returns:
        The sum of x and y.
    """
    return x + y
```

#### Service Architecture Guidelines
- Place new services under `src/backend/services/` with matching test modules under `tests/services/`
- Use SQLAlchemy models with the `Base` from `backend.db`
- For authentication, extend the existing FastAPI-Users setup in `services/auth/` and `services/users/`
- Keep modules focused: one class or related functions per file
- Update `src/backend/app.py` to include new routers with appropriate tags
- Write tests alongside new code, following naming conventions (`test_<module>.py`)

### Branching Strategy
- **`main`**: Stable, production-ready code. All finished features and fixes are merged here
- **Feature branches**: Named `feature/<short-desc>` for new features
- **Fix branches**: Named `fix/<short-desc>` for bugs
- **Chore branches**: Named `chore/<short-desc>` for non-feature work (docs, CI updates)

### Commit Messages
Use the [Conventional Commits](https://www.conventionalcommits.org/) format:
```
type(scope): short description
```
- **type**: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`
- **scope**: The area affected, e.g., `auth`, `users`, `example_service`

### Pull Request Process

1. **Ensure your branch is up to date** with `main`:
   ```bash
   git fetch origin
   git rebase origin/main
   ```

2. **Run tests and linters** locally:
   ```bash
   uv run pytest
   # Add any linting tools you use
   ```

3. **Push your branch** and open a PR against `main`:
   ```bash
   git push -u origin feature/brief-description
   ```

4. **Fill in the PR template** with:
   - Description of changes
   - Related issue number (if any)
   - Any migration steps (if DB schema changed)

5. **Request reviews** from at least one other maintainer

### Code Review Checklist

Reviewers will check:
- Code correctness and functionality
- Style and adherence to guidelines
- Test coverage
- Documentation updates
- Database migration compatibility
- Security considerations

### Database Migrations

When making database schema changes:

1. **Create migration**:
   ```bash
   uv run alembic revision --autogenerate -m "Description of changes"
   ```

2. **Review the generated migration** before committing
3. **Test migration** on both SQLite and PostgreSQL if possible
4. **Include migration** in your pull request

### Testing Requirements

- Write tests for new features and bug fixes
- Maintain or improve test coverage
- Test both SQLite and PostgreSQL compatibility when relevant
- Include integration tests for API endpoints
- Mock external services (email providers, etc.)

### Documentation Updates

- Update this README for new features or changes
- Add docstrings to new functions and classes
- Update API documentation if endpoints change
- Include configuration examples for new environment variables

### Getting Help

If you encounter issues or have questions:
- Check existing [issues](https://github.com/your-organization/backend/issues)
- Review this README and project documentation
- Ask questions in pull request discussions
- Open a new issue with detailed information

### Reporting Issues

When reporting bugs or requesting features:
1. Check existing issues to avoid duplicates
2. Use descriptive titles
3. Include steps to reproduce (for bugs)
4. Provide expected vs. actual behavior
5. Include relevant logs or screenshots

---

## 📊 Development Commands Reference

```bash
# Dependencies
uv sync                        # Install/update dependencies
uv add package-name            # Add new dependency
uv add --dev package-name      # Add development dependency

# Database
uv run alembic revision --autogenerate -m "Description"
uv run alembic upgrade head    # Apply migrations
uv run alembic downgrade -1    # Rollback one migration
uv run alembic history         # View migration history

# Development
uv run backend                 # Start server
uv run uvicorn backend.main:app --reload --log-level debug  # Debug mode

# Testing
uv run pytest                 # All tests
uv run pytest --cov --cov-report=html  # With HTML coverage
uv run pytest -x              # Stop on first failure
```

---

**Happy coding!** This backend template provides a solid foundation for building scalable FastAPI applications with authentication and database independence.
