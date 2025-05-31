# API Endpoints Summary

**API Version:** 0.1.0
**Title:** FastAPI

## Available Endpoints

### Uncategorized

- 🟢 **GET** `/`
  - **Summary:** Root
  - **Responses:** 200

### Auth

- 🔵 **POST** `/api/auth/register`
  - **Summary:** Register:Register
  - **Responses:** 201, 400, 422

- 🔵 **POST** `/api/auth/forgot-password`
  - **Summary:** Reset:Forgot Password
  - **Responses:** 202, 422

- 🔵 **POST** `/api/auth/reset-password`
  - **Summary:** Reset:Reset Password
  - **Responses:** 200, 400, 422

- 🔵 **POST** `/api/auth/request-verify-token`
  - **Summary:** Verify:Request-Token
  - **Responses:** 202, 422

- 🔵 **POST** `/api/auth/verify`
  - **Summary:** Verify:Verify
  - **Responses:** 200, 400, 422

- 🔵 **POST** `/api/auth/jwt/login`
  - **Summary:** Auth:Jwt.Login
  - **Responses:** 200, 400, 422

- 🔵 **POST** `/api/auth/jwt/logout`
  - **Summary:** Auth:Jwt.Logout
  - **Responses:** 200, 401

### Users

- 🟢 **GET** `/api/users/me`
  - **Summary:** Users:Current User
  - **Responses:** 200, 401

- 🟠 **PATCH** `/api/users/me`
  - **Summary:** Users:Patch Current User
  - **Responses:** 200, 401, 400, 422

- 🟢 **GET** `/api/users/{id}`
  - **Summary:** Users:User
  - **Responses:** 200, 401, 403, 404, 422

- 🟠 **PATCH** `/api/users/{id}`
  - **Summary:** Users:Patch User
  - **Responses:** 200, 401, 403, 404, 400, 422

- 🔴 **DELETE** `/api/users/{id}`
  - **Summary:** Users:Delete User
  - **Responses:** 204, 401, 403, 404, 422

## Data Models

### BearerResponse

- **access_token** ✳️ (`string`) - Access Token
- **token_type** ✳️ (`string`) - Token Type

### Body_auth_jwt_login_api_auth_jwt_login_post

- **grant_type** (`unknown`) - Grant Type
- **username** ✳️ (`string`) - Username
- **password** ✳️ (`string`) - Password
- **scope** (`string`) - Scope
- **client_id** (`unknown`) - Client Id
- **client_secret** (`unknown`) - Client Secret

### Body_reset_forgot_password_api_auth_forgot_password_post

- **email** ✳️ (`string`) - Email

### Body_reset_reset_password_api_auth_reset_password_post

- **token** ✳️ (`string`) - Token
- **password** ✳️ (`string`) - Password

### Body_verify_request_token_api_auth_request_verify_token_post

- **email** ✳️ (`string`) - Email

### Body_verify_verify_api_auth_verify_post

- **token** ✳️ (`string`) - Token

### ErrorModel

- **detail** ✳️ (`unknown`) - Detail

### HTTPValidationError

- **detail** (`array`) - Detail

### UserCreate

- **email** ✳️ (`string`) - Email
- **password** ✳️ (`string`) - Password
- **is_active** (`boolean`) - Is Active
- **is_superuser** (`boolean`) - Is Superuser
- **is_verified** (`boolean`) - Is Verified

### UserRead

- **id** ✳️ (`string`) - Id
- **email** ✳️ (`string`) - Email
- **is_active** ✳️ (`boolean`) - Is Active
- **is_superuser** ✳️ (`boolean`) - Is Superuser
- **is_verified** ✳️ (`boolean`) - Is Verified
- **created_at** ✳️ (`string`) - Created At

### UserUpdate

- **password** (`unknown`) - Password
- **email** (`unknown`) - Email
- **is_active** (`unknown`) - Is Active
- **is_superuser** (`unknown`) - Is Superuser
- **is_verified** (`unknown`) - Is Verified

### ValidationError

- **loc** ✳️ (`array`) - Location
- **msg** ✳️ (`string`) - Message
- **type** ✳️ (`string`) - Error Type

---

*This summary is automatically generated from the OpenAPI schema when the backend starts.*

**Legend:** ✳️ = Required field | 🟢 GET | 🔵 POST | 🟡 PUT | 🔴 DELETE | 🟠 PATCH