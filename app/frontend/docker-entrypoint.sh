#!/bin/sh
set -e

if [ "$ENVIRONMENT" = "prod" ]; then
  echo "Running in production mode..."
  # Build for production
  npm run build
  # Use a simple server to serve the built app
  npm install -g serve
  serve -s dist -l 3000
else
  echo "Running in development mode..."
  # Run development server
  npm run dev -- --host 0.0.0.0 --port 3000
fi

exec "$@"