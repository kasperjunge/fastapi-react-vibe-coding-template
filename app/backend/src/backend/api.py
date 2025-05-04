from fastapi import FastAPI
from backend.services.example_service.routes import router as example_router

app = FastAPI()

app.include_router(example_router, tags=["example"])
