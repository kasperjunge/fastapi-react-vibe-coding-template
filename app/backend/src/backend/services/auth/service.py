from fastapi import FastAPI

from supertokens_python import (
    init,
    SupertokensConfig,
    InputAppInfo,
)
from supertokens_python.recipe import session, emailpassword
from supertokens_python.framework.fastapi import get_middleware, get_routes

from backend.settings import settings


def init_supertokens(app: FastAPI) -> None:
    """Configure SuperTokens and attach its middleware and routes."""

    init(
        app_info=InputAppInfo(
            app_name="fastapi-react-vibe",
            api_domain=f"http://{settings.BACKEND_HOST}:{settings.BACKEND_PORT}",
            website_domain=settings.VITE_API_URL,
        ),
        supertokens_config=SupertokensConfig(
            connection_uri=settings.SUPERTOKENS_CONNECTION_URI,
            api_key=settings.SUPERTOKENS_API_KEY,
        ),
        framework="fastapi",
        recipe_list=[session.init(), emailpassword.init()],
    )

    app.add_middleware(get_middleware())
    app.include_router(get_routes(), prefix="/auth")

