# Database Migrations

This directory contains database migration scripts powered by Alembic.

## How to use migrations

1. **Apply migrations**: Run `alembic upgrade head` to apply all migrations to the latest version
2. **Create a new migration**: Run `alembic revision --autogenerate -m "description"` to create a new migration based on model changes
3. **Downgrade database**: Run `alembic downgrade -1` to roll back the last migration

## Directory Structure

- `env.py`: Configuration for Alembic and SQLModel integration
- `script.py.mako`: Template for migration scripts
- `versions/`: Contains individual migration scripts

## Important Notes

- Always check auto-generated migrations before applying them
- Migrations are applied automatically when the application starts
- Add new models to `env.py` to ensure they're included in migrations 