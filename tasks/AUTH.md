**Task Summary**

**Title:** Set up user authentication backend with FastAPI-Users

**Objective:**
Implement a user authentication backend using FastAPI-Users that supports:

* Password-based sign-up/login
* OAuth logins via GitHub and Google (placeholders for now)
* Email verification
* Password reset functionality
* SQLModel as ORM
* Designed to be ready for basic frontend consumption

**Technical Specifications:**

* **Framework:** FastAPI
* **Auth Library:** FastAPI-Users
* **ORM:** SQLModel
* **OAuth:** GitHub & Google (placeholders, no credentials yet)
* **Email:** Verification and reset functionality included (no provider configured yet)
* **User model:** Includes generic fields (email, hashed password, is\_active, is\_verified, created\_at)

**Constraints/Notes:**

* OAuth credentials and email service setup will be stubbed until real values are available.
* Frontend integration will come later—backend will expose necessary routes and behaviors.