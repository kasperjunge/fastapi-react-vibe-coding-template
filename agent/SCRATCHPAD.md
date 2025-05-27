# Scratchpad - Useful Information & Insights

## OpenAPI Schema Auto-Dumping (Added)

### Implementation
- **Location**: `backend/src/backend/main.py`
- **Functionality**: Automatically dumps OpenAPI schema to `agent/openapi.json` every time backend starts
- **Trigger**: Runs when executing `uv run backend`

### Technical Details
- Uses FastAPI's built-in `app.openapi()` method to generate schema
- Saves to `agent/openapi.json` in project root
- Creates agent directory if it doesn't exist
- Pretty-formatted JSON with 2-space indentation
- Error handling with console feedback
- UTF-8 encoding for proper character support

### Benefits
- Always up-to-date API documentation
- Useful for frontend development and API consumers
- Automatic generation without manual intervention
- Stored in agent/ directory for easy access by AI assistant

### Usage
```bash
uv run backend
```
Output: `✅ OpenAPI schema dumped to: /path/to/project/agent/openapi.json`
