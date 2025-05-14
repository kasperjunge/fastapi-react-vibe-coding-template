# Use Python 3.10 with uv pre-installed as base image
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY pyproject.toml uv.lock ./

# Install dependencies without installing the project itself
# This creates a separate layer for dependencies which improves build caching
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked --no-install-project

# Copy the rest of the application
COPY . .

# Set environment variables
ENV PYTHONPATH=/app

# Expose port 8000 for the FastAPI application
EXPOSE 8000

# Compile bytecode for improved startup time
ENV UV_COMPILE_BYTECODE=1

# Sync the project and run the backend
CMD uv sync --locked && uv run backend
