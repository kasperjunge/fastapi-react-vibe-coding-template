from fastapi import APIRouter, Depends
from backend.services.example_service.schemas import ExampleSchema, ExampleCreate
from backend.services.example_service.models import ExampleModel
from backend.services.example_service.service import ExampleService
from backend.db import get_db
from sqlmodel import Session

router = APIRouter()

@router.get("/example", response_model=ExampleSchema)
async def get_example(db: Session = Depends(get_db)):
    service = ExampleService()
    return service.get_example()

@router.post("/example", response_model=ExampleSchema)
async def create_example(example: ExampleCreate, db: Session = Depends(get_db)):
    service = ExampleService()
    return service.create_example(db, example.model_dump())
