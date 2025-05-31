from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.db import create_db_and_tables
from backend.services.auth.routes import router as auth_router
from backend.services.users.routes import router as users_router
from backend.settings import settings

@asynccontextmanager
async def lifespan(app: FastAPI):

    await create_db_and_tables()

    yield

app = FastAPI(lifespan=lifespan)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/api", tags=["auth"])
app.include_router(users_router, prefix="/api", tags=["users"])

@app.get("/")
async def root():
    return {"message": "Hello World"}