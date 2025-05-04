from sqlmodel import create_engine, SQLModel
from backend.settings import settings

engine = create_engine(settings.DATABASE_URL)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
    