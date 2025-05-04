import uvicorn
from backend.api import app
from backend.settings import settings

def main() -> None:
    print("Hello from backend!!")

    reload = settings.ENVIRONMENT == "local"

    uvicorn.run(
        "backend.main:app", 
        host="0.0.0.0", 
        port=8000, 
        reload=reload
    )

if __name__ == "__main__":
    main()