# FastAPI Backend Template

A modern, production-ready backend template built with FastAPI, SQLModel, and Pydantic.

## Features

- **FastAPI**: High-performance, easy-to-learn, fast to code, ready for production
- **SQLModel**: SQL databases in Python with the power of SQLAlchemy and the simplicity of Pydantic
- **Pydantic**: Data validation and settings management using Python type hints
- **Service-oriented architecture**: Modular structure for maintainability and scalability
- **Docker support**: Ready for containerized deployment

## Project Structure

```
backend/
├── src/                    # Source code directory
│   └── backend/            # Main application package
│       ├── api.py          # API setup and configuration
│       ├── database.py     # Database connection and session management
│       ├── dependencies.py # Dependency injection components
│       ├── settings.py     # Application settings and configuration
│       ├── main.py         # Application entry point
│       └── services/       # Service modules (feature-based)
│           └── example_service/  # Example service module
│               ├── models.py     # SQLModel models
│               ├── schemas.py    # Additional schemas for request/response validation
│               ├── routes.py     # API route definitions
│               └── service.py    # Business logic implementation
├── tests/                  # Test directory
│   ├── test_api.py         # Tests for api.py
│   ├── test_database.py    # Tests for database.py
│   ├── test_dependencies.py # Tests for dependencies.py
│   ├── test_main.py        # Tests for main.py
│   ├── test_settings.py    # Tests for settings.py
│   └── services/           # Tests for service modules
│       └── example_service/ # Tests for example service
│           ├── test_models.py    # Tests for models.py
│           ├── test_routes.py    # Tests for routes.py
│           ├── test_schemas.py   # Tests for schemas.py
│           └── test_service.py   # Tests for service.py
├── pyproject.toml          # Project metadata and dependencies
├── uv.lock                 # Lock file for dependencies
├── .python-version         # Python version specification
├── Dockerfile              # Docker container definition 
└── README.md               # Project documentation
```

## Getting Started

### Local Development

Install enviroment:
```bash
uv sync
```

Run the backend:
```bash
uv run backend
```

### Testing

Run all tests:
```bash
uv run pytest
```

## Adding a New Service

1. Create a new directory in `src/backend/services/`
2. Implement `models.py` using SQLModel, plus any additional schemas in `schemas.py` 
3. Implement business logic in `service.py`
4. Create API endpoints in `routes.py`
5. Register the router in `src/backend/api.py`
6. Create corresponding test files in `tests/services/your_service/`
\n## Authentication\nThis project includes a simple authentication service with JWT-based login, email verification and password reset.
