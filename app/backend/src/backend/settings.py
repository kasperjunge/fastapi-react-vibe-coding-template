import pathlib
from pydantic_settings import BaseSettings

env_file_path = pathlib.Path(__file__).absolute().parents[4] / ".env"
class Settings(BaseSettings):

    # Environment (local, dev, prod)
    ENVIRONMENT: str

    # Postgres DB
    PGHOST: str
    PGPORT: str
    PGDATABASE: str
    PGUSER: str
    PGPASSWORD: str

    # Backend
    BACKEND_PORT: int
    BACKEND_HOST: str

    # Frontend
    VITE_API_URL: str

    class Config:
        env_file = env_file_path
        env_file_encoding = "utf-8"

    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql://{self.PGUSER}:{self.PGPASSWORD}@{self.PGHOST}:{self.PGPORT}/{self.PGDATABASE}"

settings = Settings()