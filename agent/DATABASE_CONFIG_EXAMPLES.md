# Database Configuration Examples

This document provides examples of how to configure the application for different database setups.

## Environment Variables

Create a `.env` file in the project root with the following configuration:

### SQLite Configuration (Default for Development)

```bash
# Environment Configuration
ENVIRONMENT=dev

# Database Configuration
DATABASE_TYPE=sqlite
SQLITE_DB_PATH=./data/app.db

# Server Configuration
BACKEND_HOST=localhost
BACKEND_PORT=8000
VITE_API_URL=http://localhost:8000
FRONTEND_PORT=3000

# Admin User Configuration
ADMIN_EMAIL=admin@example.com
ADMIN_USERNAME=admin
ADMIN_PASSWORD=admin123
ADMIN_FIRST_NAME=Admin
ADMIN_LAST_NAME=User

# Security Configuration
SECRET_KEY=your-secret-key-here-change-in-production

# Email Configuration
EMAIL_PROVIDER=mailhog
MAIL_USERNAME=
MAIL_PASSWORD=
MAIL_FROM=
MAIL_PORT=587
MAIL_SERVER=localhost
MAIL_FROM_NAME=FastAPI App
MAIL_STARTTLS=true
MAIL_SSL_TLS=false
USE_CREDENTIALS=true
VALIDATE_CERTS=true
RESEND_API_KEY=
VERIFICATION_TOKEN_EXPIRE_HOURS=24
```

### PostgreSQL Configuration (Production)

```bash
# Environment Configuration
ENVIRONMENT=prod

# Database Configuration
DATABASE_TYPE=postgresql
POSTGRES_HOST=your-postgres-host.com
POSTGRES_PORT=5432
POSTGRES_DB=prod_db
POSTGRES_USER=prod_user
POSTGRES_PASSWORD=secure-production-password

# Server Configuration
BACKEND_HOST=0.0.0.0
BACKEND_PORT=8000
VITE_API_URL=https://your-api-domain.com
FRONTEND_PORT=3000

# Admin User Configuration
ADMIN_EMAIL=admin@yourdomain.com
ADMIN_USERNAME=admin
ADMIN_PASSWORD=secure-admin-password
ADMIN_FIRST_NAME=Admin
ADMIN_LAST_NAME=User

# Security Configuration
SECRET_KEY=very-secure-secret-key-for-production

# Email Configuration (Production with Resend)
EMAIL_PROVIDER=resend
RESEND_API_KEY=your-resend-api-key
MAIL_FROM=noreply@yourdomain.com
MAIL_FROM_NAME=Your App Name
VERIFICATION_TOKEN_EXPIRE_HOURS=24
```

### PostgreSQL Development Configuration

```bash
# Environment Configuration
ENVIRONMENT=dev

# Database Configuration
DATABASE_TYPE=postgresql
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=dev_db
POSTGRES_USER=dev_user
POSTGRES_PASSWORD=dev_password

# Server Configuration
BACKEND_HOST=localhost
BACKEND_PORT=8000
VITE_API_URL=http://localhost:8000
FRONTEND_PORT=3000

# Admin User Configuration
ADMIN_EMAIL=admin@example.com
ADMIN_USERNAME=admin
ADMIN_PASSWORD=admin123
ADMIN_FIRST_NAME=Admin
ADMIN_LAST_NAME=User

# Security Configuration
SECRET_KEY=dev-secret-key

# Email Configuration (Development with MailHog)
EMAIL_PROVIDER=mailhog
MAIL_USERNAME=
MAIL_PASSWORD=
MAIL_FROM=
MAIL_PORT=587
MAIL_SERVER=localhost
MAIL_FROM_NAME=FastAPI App
MAIL_STARTTLS=true
MAIL_SSL_TLS=false
USE_CREDENTIALS=true
VALIDATE_CERTS=true
VERIFICATION_TOKEN_EXPIRE_HOURS=24
```

## Database Setup Instructions

### SQLite Setup (Default)

1. No additional setup required
2. Database file will be created automatically at the specified path
3. Directory structure will be created if it doesn't exist

```bash
# Start the application
cd backend
uv run alembic upgrade head
uv run backend
```

### PostgreSQL Setup

#### Using Docker (Recommended for Development)

```bash
# Start PostgreSQL container
docker run --name local-postgres \
  -e POSTGRES_DB=dev_db \
  -e POSTGRES_USER=dev_user \
  -e POSTGRES_PASSWORD=dev_password \
  -p 5432:5432 \
  -v pgdata:/var/lib/postgresql/data \
  -d postgres

# Run migrations and start application
cd backend
uv run alembic upgrade head
uv run backend
```

#### Using Docker Compose

```bash
# From project root
docker-compose up -d db

# Run migrations and start application
cd backend
uv run alembic upgrade head
uv run backend
```

#### Production PostgreSQL

1. Set up your PostgreSQL instance (cloud provider, self-hosted, etc.)
2. Create database and user
3. Configure environment variables
4. Run migrations

```bash
cd backend
uv run alembic upgrade head
uv run backend
```

## Migration Commands

### Create New Migration

```bash
cd backend
uv run alembic revision --autogenerate -m "Description of changes"
```

### Apply Migrations

```bash
cd backend
uv run alembic upgrade head
```

### Rollback Migration

```bash
cd backend
uv run alembic downgrade -1
```

## Switching Between Databases

To switch from SQLite to PostgreSQL or vice versa:

1. Update the `DATABASE_TYPE` in your `.env` file
2. Configure the appropriate database settings
3. Run migrations: `uv run alembic upgrade head`
4. Restart the application

**Note**: Data will not be automatically migrated between different database types. You'll need to export/import data manually if switching databases with existing data.

## Troubleshooting

### SQLite Issues

- **Permission errors**: Ensure the application has write access to the database directory
- **Database locked**: Make sure no other processes are accessing the database file
- **Path issues**: Use absolute paths if relative paths cause problems

### PostgreSQL Issues

- **Connection refused**: Verify PostgreSQL is running and accessible
- **Authentication failed**: Check username, password, and database name
- **Database doesn't exist**: Create the database before running migrations
- **Port conflicts**: Ensure PostgreSQL port (default 5432) is not in use by other services

### General Issues

- **Migration errors**: Check that all required environment variables are set
- **Import errors**: Ensure all dependencies are installed (`uv sync`)
- **Configuration errors**: Validate your `.env` file syntax and values 