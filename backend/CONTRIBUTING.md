# Contributing to the Backend

Thank you for considering contributing to this FastAPI backend! We welcome improvements, bug fixes, and new features. To ensure a smooth process, please follow the guidelines below.

---

## Table of Contents

- [Contributing to the Backend](#contributing-to-the-backend)
  - [Table of Contents](#table-of-contents)
  - [Getting Started](#getting-started)
  - [Reporting Issues](#reporting-issues)
  - [Development Workflow](#development-workflow)
  - [Branching Strategy](#branching-strategy)
  - [Coding Guidelines](#coding-guidelines)
  - [Project Structure](#project-structure)
  - [Commit Messages](#commit-messages)
  - [Testing](#testing)
  - [Pull Request Process](#pull-request-process)
  - [Code Review](#code-review)
  - [License](#license)

---

## Getting Started

1. **Fork the repository** and clone your fork:

   ```bash
   git clone https://github.com/your-organization/backend.git
   cd backend
   ```
2. **Install dependencies** in a Python 3.12+ environment:

   ```bash
   uv sync
   ```
3. **Create a `.env` file** at the project root (one directory above `backend/`). Copy the provided `.env.example` and rename it:

   ```bash
   cp .env.example .env
   ```

   This `.env` file will be read by `settings.py` to configure the application.
4. **Run migrations** and start the development server:

   ```bash
   uv run backend
   ```
5. **Verify** the API is running at `http://localhost:8000`.

---

## Reporting Issues

If you encounter a bug or have a feature request:

1. Check existing [issues](https://github.com/your-organization/backend/issues) to see if it's been reported.
2. If not, open a new issue with:

   * A descriptive title
   * Steps to reproduce (for bugs)
   * Expected vs. actual behavior
   * Relevant logs or screenshots

---

## Development Workflow

1. Create a branch for your work:

   ```bash
   git checkout -b feature/brief-description
   ```
2. Commit logically related changes.
3. Rebase or merge from `main` to keep your branch up to date:

   ```bash
   git fetch origin
   git rebase origin/main
   ```
4. Push your branch to your fork:

   ```bash
   git push -u origin feature/brief-description
   ```

---

## Branching Strategy

* **`main`**: Stable, production-ready code. All finished features and fixes are merged here.
* **Feature branches**: Named `feature/<short-desc>` for new features.
* **Fix branches**: Named `fix/<short-desc>` for bugs.
* **Chore branches**: Named `chore/<short-desc>` for non-feature work (docs, CI updates).

---

## Coding Guidelines

* **Language & Framework**: Python 3.12, FastAPI, SQLModel.
* **Formatting**: Follow [PEP 8](https://peps.python.org/pep-0008/).
* **Imports**: Group standard library, third-party, and local imports separately.
* **Type Hints**: Use Python type annotations consistently.
* **Docstrings**: Use Google style docstrings for modules, classes, functions, and methods:

  ```python
  def add(x: int, y: int) -> int:
      """
      Add two integers.

      Args:
          x: First integer.
          y: Second integer.

      Returns:
          The sum of x and y.
      """
      return x + y
  ```

---

## Project Structure

Organize new code following the existing service-oriented layout:

```
backend/
├── src/backend/
│   ├── services/
│   │   └── your_service/
│   │       ├── models.py    # SQLModel definitions
│   │       ├── schemas.py   # Pydantic schemas
│   │       ├── service.py   # Business logic
│   │       └── routes.py    # API routes
│   ├── api.py              # Register routers
│   ├── db.py               # Engine & session
│   ├── main.py             # Entry point
│   └── settings.py         # Configurations
├── migrations/             # Alembic files
├── tests/                  # Mirror src structure for tests
└── Dockerfile
```

**Guidelines:**

* Place new services under `src/backend/services/` with matching test modules under `tests/services/`.
* Keep modules focused: one class or related functions per file.
* Update `src/backend/api.py` to include new routers with appropriate tags.
* Write tests alongside new code, following naming conventions (`test_<module>.py`).

---

## Commit Messages

* Use the [Conventional Commits](https://www.conventionalcommits.org/) format:

  ```
  type(scope): short description
  ```
* **type**: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`
* **scope**: The area affected, e.g., `auth`, `example_service`.

---

## Testing

* Tests live under `tests/` mirroring `src/backend` structure.
* Run the full test suite:

  ```bash
  uv run pytest
  ```
* Aim for high coverage on new features and bug fixes.

---

## Pull Request Process

1. Ensure your branch is up to date with `main`.
2. Run tests and linters locally.
3. Push your branch and open a PR against `main`.
4. Fill in the PR template with:

   * Description of changes
   * Related issue number (if any)
   * Any migration steps (if DB schema changed)
5. Request reviews from at least one other maintainer.

---

## Code Review

* Reviewers will check:

  * Code correctness and functionality
  * Style and adherence to guidelines
  * Test coverage
  * Documentation updates
* Address review comments promptly.

---

## License

This project is licensed under the [MIT License](LICENSE).
