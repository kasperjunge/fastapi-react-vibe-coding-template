import json
from pathlib import Path
import uvicorn
from backend.settings import settings
from backend.app import app

def dump_openapi_schema() -> None:
    """Dump the OpenAPI schema to a JSON file in the agent/ directory."""
    try:
        # Get the OpenAPI schema from the FastAPI app
        openapi_schema = app.openapi()
        
        # Define the output path (agent/ directory in project root)
        project_root = Path(__file__).parent.parent.parent.parent
        agent_dir = project_root / "agent"
        schema_path = agent_dir / "openapi.json"
        
        # Ensure the agent directory exists
        agent_dir.mkdir(exist_ok=True)
        
        # Write the schema to file
        with open(schema_path, "w", encoding="utf-8") as f:
            json.dump(openapi_schema, f, indent=2, ensure_ascii=False)
        
        print(f"✅ OpenAPI schema dumped to: {schema_path}")
        
    except Exception as e:
        print(f"❌ Failed to dump OpenAPI schema: {e}")

def main() -> None:
    print("Hello from backend!!")
    
    # Dump OpenAPI schema before starting the server
    dump_openapi_schema()

    reload = settings.ENVIRONMENT == "dev"

    uvicorn.run(
        "backend.main:app", 
        host=settings.BACKEND_HOST, 
        port=settings.BACKEND_PORT, 
        reload=reload
    )

if __name__ == "__main__":
    main()