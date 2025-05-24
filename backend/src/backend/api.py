from contextlib import asynccontextmanager
from fastapi import FastAPI
from backend.services.example_service.routes import router as example_router
from backend.db import run_migrations, create_db_and_tables, engine
from sqlmodel import Session

@asynccontextmanager
async def lifespan(app: FastAPI):

    create_db_and_tables()
    run_migrations()

    yield

app = FastAPI(lifespan=lifespan)

app.include_router(example_router, tags=["example"])

@app.get("/")
async def root():
    return {"message": "Hello World"}