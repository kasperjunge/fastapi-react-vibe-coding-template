from sqlmodel import select
from backend.services.example_service.models import ExampleModel

class ExampleService:
    def __init__(self):
        pass

    def get_example(self):
        # This is just a placeholder. In a real app, you'd use the session to query data
        return {"message": "Hello, World!"}
    
    def get_example_by_id(self, session, example_id: int):
        return session.exec(select(ExampleModel).where(ExampleModel.id == example_id)).first()
    
    def create_example(self, session, example_data):
        db_example = ExampleModel(**example_data)
        session.add(db_example)
        session.commit()
        session.refresh(db_example)
        return db_example
