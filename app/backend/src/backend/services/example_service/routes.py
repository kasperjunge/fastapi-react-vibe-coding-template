from fastapi import APIRouter
from backend.services.example_service.schemas import ExampleSchema, ExampleCreate
from backend.services.example_service.models import ExampleModel
from backend.services.example_service.service import ExampleService
from backend.dependencies import SessionDep

router = APIRouter()

@router.get("/example", response_model=ExampleSchema)
async def get_example(session: SessionDep):
    service = ExampleService()
    return service.get_example()

@router.post("/example", response_model=ExampleSchema)
async def create_example(example: ExampleCreate, session: SessionDep):
    service = ExampleService()
    return service.create_example(session, example.model_dump())
