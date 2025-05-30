#!/bin/bash

# Development script for FastAPI-React template
# Creates a tmux session with 4 separate windows for development

SESSION_NAME="fastapi-react-dev"

# Check if tmux session already exists
if tmux has-session -t $SESSION_NAME 2>/dev/null; then
    echo "Session $SESSION_NAME already exists. Attaching..."
    tmux attach-session -t $SESSION_NAME
    exit 0
fi

# Get the current directory (project root)
PROJECT_ROOT=$(pwd)

# Create new tmux session with first window (Backend)
tmux new-session -d -s $SESSION_NAME -c "$PROJECT_ROOT/backend" -n "Backend"
tmux send-keys -t $SESSION_NAME:Backend "echo 'Starting Backend...' && uv run backend" Enter

# Create Frontend window
tmux new-window -t $SESSION_NAME -c "$PROJECT_ROOT/frontend" -n "Frontend"
tmux send-keys -t $SESSION_NAME:Frontend "echo 'Starting Frontend...' && npm run dev" Enter

# Create Database window
tmux new-window -t $SESSION_NAME -c "$PROJECT_ROOT" -n "Database"
tmux send-keys -t $SESSION_NAME:Database "echo 'Database Shell (run the command when ready):' && echo 'docker exec -it local-postgres psql -U postgres -d db'" Enter

# Create Mailhog window
tmux new-window -t $SESSION_NAME -c "$PROJECT_ROOT" -n "Mailhog"
tmux send-keys -t $SESSION_NAME:Mailhog "echo 'Starting Mailhog...' && mailhog" Enter

# Select the Backend window to start
tmux select-window -t $SESSION_NAME:Backend

# Attach to the session
echo "Starting development environment..."
echo "Backend: http://localhost:8000"
echo "Frontend: http://localhost:3000"
echo "Mailhog: http://localhost:8025"
echo ""
echo "Windows created:"
echo "  0: Backend"
echo "  1: Frontend"
echo "  2: Database"
echo "  3: Mailhog"
echo ""
echo "Use Ctrl+B then number (0-3) to switch between windows"
echo "Use Ctrl+B then 'n' for next window, 'p' for previous window"
echo "Use Ctrl+B then 'd' to detach from session"
echo "Use 'tmux attach-session -t $SESSION_NAME' to reattach"
echo ""

tmux attach-session -t $SESSION_NAME 