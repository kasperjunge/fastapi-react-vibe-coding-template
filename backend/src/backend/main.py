import json
from pathlib import Path
import uvicorn
from backend.settings import settings
from backend.app import app
from backend.utils import dump_openapi_schema_and_summary

def main() -> None:
    print("Hello from backend!!")
    
    # Dump OpenAPI schema and generate summary before starting the server
    dump_openapi_schema_and_summary(app)

    reload = settings.ENVIRONMENT == "dev"

    uvicorn.run(
        "backend.main:app", 
        host=settings.BACKEND_HOST, 
        port=settings.BACKEND_PORT, 
        reload=reload
    )

if __name__ == "__main__":
    main()