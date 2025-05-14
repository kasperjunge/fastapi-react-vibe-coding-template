- Implement JWT Auth# Auth and Users Services Implementation Plan

## Backend Implementation

### 1. User Model (models.py) ✅
- Create SQLModel class with the following fields:
  - id (UUID, primary key)
  - email (unique, indexed)
  - password_hash (string, not exposed in responses)
  - name
  - is_active (boolean, default true)
  - is_verified (boolean, default false)
  - role (enum: 'user'/'admin', default 'user')
  - created_at, updated_at (datetime)

### 2. Authentication Service (service.py)
- Password utilities:
  - hash_password(): Uses bcrypt to hash passwords
  - verify_password(): Compares plain password with hash
- JWT utilities:
  - create_access_token(): Generates JWT with configurable expiry
  - create_refresh_token(): Creates longer-lived refresh token
  - verify_token(): Validates token and extracts payload
- User authentication methods:
  - authenticate_user(): Verifies credentials
  - get_current_user(): Gets user from token

### 3. Auth Routes (routes.py)
- POST /auth/register: Create new user
- POST /auth/login: Authenticate and return tokens
- POST /auth/refresh: Generate new access token
- GET /auth/me: Get current user profile
- POST /auth/logout: Invalidate tokens

### 4. User Service (service.py)
- create_user(): Register a new user
- get_user(): Get user by ID or email
- update_user(): Update user profile
- delete_user(): Deactivate/delete user
- list_users(): Get paginated list of users (admin only)

### 5. User Routes (routes.py)
- GET /users: List users (admin only)
- GET /users/{id}: Get user by ID
- PUT /users/{id}: Update user
- DELETE /users/{id}: Delete user

### 6. Auth Dependencies (dependencies.py)
- get_current_user(): Extracts and validates JWT from requests
- get_current_active_user(): Ensures user is active
- get_current_admin_user(): Ensures user has admin role

### 7. Configuration (settings.py)
- Add JWT settings:
  - SECRET_KEY
  - TOKEN_EXPIRE_MINUTES
  - REFRESH_TOKEN_EXPIRE_DAYS
  - ALGORITHM (default HS256)

## Frontend Integration
- Update existing frontend auth service to connect with new backend endpoints
- Add token refresh mechanism in API service
- Update AuthContext to handle token refresh

## Future Enhancements (not implemented initially)
- Email verification flow
- Password reset functionality
- Session management
- Rate limiting for auth endpoints

Would you like me to clarify or expand on any part of this plan?
