from typing import Annotated

from fastapi import Depends
from sqlmodel import Session

from backend.database import get_session

# Type annotation for dependency injection
SessionDep = Annotated[Session, Depends(get_session)]


# Additional dependencies can be added here as needed:
# For example, authentication dependencies, etc.
