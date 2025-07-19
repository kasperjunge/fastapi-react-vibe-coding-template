# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Environment

**Python Backend:** Use `uv` for Python environment management:
- Install environment: `uv sync`
- Add packages: `uv add package-name` or `uv add --dev package-name`
- Run commands in environment: `uv run <command>`

**Frontend:** Standard Node.js with npm.

## Common Development Commands

### Backend (FastAPI)
- **Start dev server:** `cd backend && uv run backend`
- **Run tests:** `uv run pytest`
- **Run tests with coverage:** `uv run pytest --cov=backend --cov-report=html`
- **Run single test file:** `uv run pytest tests/services/users/test_users_service.py`
- **Database migrations:** 
  - Apply: `uv run alembic upgrade head`
  - Create: `uv run alembic revision --autogenerate -m "description"`
- **Install dependencies:** `uv sync`

### Frontend (React)
- **Start dev server:** `cd frontend && npm run dev`
- **Build:** `npm run build`
- **Lint:** `npm run lint`
- **Preview build:** `npm run preview`

## Architecture Overview

### Backend Structure
- **Service-oriented architecture** with services organized by domain (`auth/`, `users/`, `email/`)
- Each service contains: `models.py`, `schemas.py`, `routes.py`, `service.py`, `dependencies.py`
- **FastAPI Users** for authentication with JWT tokens and email verification
- **Async SQLAlchemy** with support for both SQLite and PostgreSQL
- **Database migrations** handled by Alembic
- **Event-driven email notifications** on user lifecycle events
- **API structure:** `/api/auth/*` for authentication, `/api/users/*` for user management

### Frontend Structure
- **Modern React 19** with TypeScript and Vite
- **TailwindCSS v4** for styling with shadcn/ui component library
- **Zustand** for client-side state management
- **TanStack Query** for server state and API calls
- **React Router DOM v7** for routing
- **Path alias:** `@/` points to `src/` directory

### Key Technologies
- **Backend:** FastAPI, SQLAlchemy, FastAPI-Users, Alembic, Pydantic, uv
- **Frontend:** React 19, TypeScript, Vite, TailwindCSS, Zustand, TanStack Query
- **Database:** SQLite / PostgreSQL
- **Authentication:** JWT tokens with email verification

## Project Structure
```
├── backend/          # Python FastAPI application
├── frontend/         # React TypeScript application  
├── docs/            # Documentation and agent commands
└── env.example      # Environment configuration template
```

## Environment Setup
- Backend runs on `http://localhost:8000` (API docs at `/docs`)
- Frontend runs on `http://localhost:5173`
- Database type controlled by `DATABASE_TYPE` environment variable
- All services support both development (SQLite) and production (PostgreSQL) configurations

## Testing
- **Backend:** pytest with async support, 80% coverage requirement
- **Test command:** `uv run pytest` from backend directory
- **Coverage:** Available in HTML format after running coverage command