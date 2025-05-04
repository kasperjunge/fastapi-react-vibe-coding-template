from fastapi import APIRouter
from backend.services.example_service.schemas import ExampleSchema
from backend.services.example_service.models import ExampleModel
from backend.services.example_service.service import ExampleService

router = APIRouter()

@router.get("/example", response_model=ExampleSchema)
async def get_example():
    service = ExampleService()
    return service.get_example()
