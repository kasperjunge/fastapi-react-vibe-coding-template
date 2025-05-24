from contextlib import asynccontextmanager

from fastapi import FastAPI

from backend.db import create_db_and_tables, run_migrations
from backend.services.example_service.routes import router as example_router
from backend.services.auth.routes import router as auth_router


@asynccontextmanager
def lifespan(app: FastAPI):
    create_db_and_tables()
    run_migrations()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(example_router, tags=["example"])
app.include_router(auth_router, tags=["auth"])


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Hello World"}
