import json
from pathlib import Path
from typing import Dict, Any


def format_method_color(method: str) -> str:
    """Add color-coded badges for HTTP methods."""
    colors = {
        'GET': '🟢',
        'POST': '🔵', 
        'PUT': '🟡',
        'DELETE': '🔴',
        'PATCH': '🟠'
    }
    return f"{colors.get(method.upper(), '⚪')} **{method.upper()}**"


def generate_openapi_summary(openapi_schema: Dict[str, Any]) -> str:
    """Generate a concise Markdown summary of the OpenAPI schema."""
    
    lines = [
        "# API Endpoints Summary",
        "",
        f"**API Version:** {openapi_schema.get('info', {}).get('version', 'N/A')}",
        f"**Title:** {openapi_schema.get('info', {}).get('title', 'N/A')}",
        "",
        "## Available Endpoints",
        ""
    ]
    
    # Group endpoints by tags/categories
    paths = openapi_schema.get('paths', {})
    endpoints_by_tag = {}
    
    for path, methods in paths.items():
        for method, details in methods.items():
            if method.lower() in ['get', 'post', 'put', 'delete', 'patch']:
                tags = details.get('tags', ['Uncategorized'])
                primary_tag = tags[0] if tags else 'Uncategorized'
                
                if primary_tag not in endpoints_by_tag:
                    endpoints_by_tag[primary_tag] = []
                
                endpoint_info = {
                    'path': path,
                    'method': method.upper(),
                    'summary': details.get('summary', 'No summary'),
                    'operation_id': details.get('operationId', ''),
                    'responses': list(details.get('responses', {}).keys())
                }
                endpoints_by_tag[primary_tag].append(endpoint_info)
    
    # Generate markdown for each category
    for tag, endpoints in sorted(endpoints_by_tag.items()):
        lines.append(f"### {tag.title()}")
        lines.append("")
        
        for endpoint in endpoints:
            method_badge = format_method_color(endpoint['method'])
            lines.append(f"- {method_badge} `{endpoint['path']}`")
            lines.append(f"  - **Summary:** {endpoint['summary']}")
            if endpoint['responses']:
                response_codes = ', '.join(endpoint['responses'])
                lines.append(f"  - **Responses:** {response_codes}")
            lines.append("")
    
    # Add schemas summary
    components = openapi_schema.get('components', {})
    schemas = components.get('schemas', {})
    
    if schemas:
        lines.append("## Data Models")
        lines.append("")
        
        for schema_name, schema_details in sorted(schemas.items()):
            if 'properties' in schema_details:
                properties = schema_details['properties']
                required_fields = schema_details.get('required', [])
                
                lines.append(f"### {schema_name}")
                lines.append("")
                
                for prop_name, prop_details in properties.items():
                    prop_type = prop_details.get('type', 'unknown')
                    is_required = " ✳️" if prop_name in required_fields else ""
                    title = prop_details.get('title', '')
                    description = prop_details.get('description', '')
                    
                    prop_info = f"- **{prop_name}**{is_required} (`{prop_type}`)"
                    if title and title != prop_name:
                        prop_info += f" - {title}"
                    if description:
                        prop_info += f" - {description}"
                    
                    lines.append(prop_info)
                
                lines.append("")
    
    # Add footer
    lines.extend([
        "---",
        "",
        "*This summary is automatically generated from the OpenAPI schema when the backend starts.*",
        "",
        f"**Legend:** ✳️ = Required field | 🟢 GET | 🔵 POST | 🟡 PUT | 🔴 DELETE | 🟠 PATCH"
    ])
    
    return "\n".join(lines)


def dump_openapi_schema_and_summary(app) -> None:
    """Dump the OpenAPI schema to JSON and generate a Markdown summary in the agent/ directory."""
    try:
        # Get the OpenAPI schema from the FastAPI app
        openapi_schema = app.openapi()
        
        # Define the output paths (agent/ directory in project root)
        project_root = Path(__file__).parent.parent.parent.parent
        agent_dir = project_root / "agent"
        schema_path = agent_dir / "openapi.json"
        summary_path = agent_dir / "API_SUMMARY.md"
        
        # Ensure the agent directory exists
        agent_dir.mkdir(exist_ok=True)
        
        # Write the full schema to JSON file
        with open(schema_path, "w", encoding="utf-8") as f:
            json.dump(openapi_schema, f, indent=2, ensure_ascii=False)
        
        # Generate and write the Markdown summary
        markdown_summary = generate_openapi_summary(openapi_schema)
        with open(summary_path, "w", encoding="utf-8") as f:
            f.write(markdown_summary)
        
        print(f"✅ OpenAPI schema dumped to: {schema_path}")
        print(f"✅ API summary generated: {summary_path}")
        
    except Exception as e:
        print(f"❌ Failed to dump OpenAPI schema: {e}") 