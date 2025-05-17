from contextlib import asynccontextmanager
from fastapi import FastAPI
from backend.services.example_service.routes import router as example_router
from backend.services.auth.routes import router as auth_router
from backend.services.users.routes import router as users_router
from backend.db import run_migrations

@asynccontextmanager
async def lifespan(app: FastAPI):
    run_migrations()
    yield

app = FastAPI()

app.include_router(auth_router, tags=["auth"])
app.include_router(users_router, tags=["users"])
app.include_router(example_router, tags=["example"])

@app.get("/")
async def root():
    return {"message": "Hello World"}