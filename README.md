# fastapi-react-vibe-coding-template

## todo
- auth
- email verification + restore password
- logging

# admin

## Authentication with SuperTokens

This project now uses [SuperTokens](https://supertokens.com/docs) for all
authentication features. The initialization happens in
`backend/services/auth/service.py`, which attaches the required middleware and
routes directly to the FastAPI application.

The Docker setup now includes a self-hosted SuperTokens core using PostgreSQL.
The backend connects to it via the `SUPERTOKENS_CONNECTION_URI` variable and the
core uses `SUPERTOKENS_DB_URI` to access the database. See `docker-compose.yml`
for configuration details.

### Running backend tests

```
cd app/backend
pytest
```
