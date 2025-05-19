from contextlib import asynccontextmanager
from fastapi import FastAPI
from backend.services.example_service.routes import router as example_router
from backend.services.auth.routes import router as auth_router
from backend.services.users.routes import router as users_router
from backend.db import run_migrations, create_db_and_tables, engine
from backend.services.users.utils import create_admin_user
from sqlmodel import Session

@asynccontextmanager
async def lifespan(app: FastAPI):

    create_db_and_tables()
    run_migrations()

    with Session(engine) as db:
        create_admin_user(db)

    yield

app = FastAPI()

app.include_router(auth_router, tags=["auth"])
app.include_router(users_router, tags=["users"])
app.include_router(example_router, tags=["example"])

@app.get("/")
async def root():
    return {"message": "Hello World"}