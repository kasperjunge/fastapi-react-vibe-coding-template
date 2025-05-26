import uvicorn
from backend.settings import settings
from backend.app import app

def main() -> None:
    print("Hello from backend!!")

    reload = settings.ENVIRONMENT == "dev"

    uvicorn.run(
        "backend.main:app", 
        host=settings.BACKEND_HOST, 
        port=settings.BACKEND_PORT, 
        reload=reload
    )

if __name__ == "__main__":
    main()