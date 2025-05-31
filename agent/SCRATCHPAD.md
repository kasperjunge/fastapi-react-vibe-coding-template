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

## .env File Analysis & Recommendations (Latest Review)

### ⚠️ Critical Issues Found:
1. **Missing DATABASE_TYPE**: Required for database independence feature
2. **Weak SECRET_KEY**: "blabla" is not secure for any environment
3. **Weak ADMIN_PASSWORD**: "1234567890" is not secure
4. **Missing VITE_API_URL**: Frontend needs this for API communication
5. **Inconsistent Email Config**: Some boolean values as strings instead of booleans

### 🔧 Security Improvements Needed:
- Generate strong SECRET_KEY (32+ characters, random)
- Use secure admin password with complexity requirements
- Consider using environment-specific secrets management
- Add CORS configuration variables
- Add rate limiting configuration

### 📝 Configuration Best Practices:
- Use .env.example for documentation
- Separate .env files per environment (.env.dev, .env.prod)
- Use proper boolean values (true/false not strings)
- Add validation for required variables
- Consider using encrypted secrets for production
