✅ 1 — Schema & Migrations

1.1 Include all models in Alembic migrations

Why Current migrations only know ExampleModel; prod DB may drift.
What
	•	Update app/backend/migrations/env.py to import every model package (backend.services.users.models, any future ones).
	•	Run alembic revision --autogenerate -m "add user tables" and commit script.
	•	CI fails if alembic upgrade heads --sql shows no changes after model edits.
Hints Add a loop that importlib.import_module‑scans backend.services.*.models.

⸻

1.2 Create relational mapping between User and OAuthAccount

Why Simplifies joins, enables eager‑loading.
What
	•	In users/models.py add

oauth_accounts: list["OAuthAccount"] = Relationship(back_populates="user")

and reciprocal property on OAuthAccount.

	•	Autogenerate migration to add the FK (already exists) and back‑ref metadata.
	•	Adjust any select(...) calls so they can options(selectinload(User.oauth_accounts)).

⸻

1.3 Add DB‑level unique constraint (provider, provider_user_id)

Why Prevents duplicate OAuth accounts.
What
	•	Alembic op:

op.create_unique_constraint(
    'uq_oauth_provider_user',
    'oauthaccount',
    ['provider', 'provider_user_id'],
)


	•	Unit test: trying to insert same pair twice must raise IntegrityError.

⸻

1.4 Fail fast on schema drift at startup

Why Guarantees dev/prod parity.
What
	•	In backend.database.create_db_and_tables() compare inspect(engine).get_table_names() with SQLModel.metadata.tables; raise & log if mismatch.
	•	Provide env flag ALLOW_SCHEMA_DRIFT=false to toggle.

⸻

2 — Cryptography & Tokens

2.1 Upgrade password hashing policy

Why Argon2 is safer; bcrypt rounds configurable.
What
	•	Switch to passlib.hash.argon2 or raise bcrypt rounds to ≥ 12 via CryptContext(..., bcrypt__rounds=12).
	•	Migration script to re‑hash on next successful login (lazy upgrade).
	•	Unit test: verify_password() accepts old & new hashes.

⸻

2.2 Add iat and nbf claims to JWT

Why Mitigates clock‑skew / replay.
What
	•	create_token() must inject "iat": utcnow, "nbf": utcnow (or utcnow‑5s leeway).
	•	decode_token() validates nbf.

⸻

2.3 Move algorithm & key management to settings

Why Preps for future RS256 rotation.
What
	•	Add JWT_ALGORITHM & optional JWT_PUBLIC_KEY_PATH to settings.py.
	•	Refactor utilities to read these instead of literals.
	•	Document rotation procedure in README.md.

⸻

2.4 Persist & rotate refresh tokens

Why Current refresh token never stored → cannot be revoked.
What
	•	Create table refresh_token(id, user_id, token, expires_at, revoked_at).
	•	Endpoint POST /auth/refresh that:
	1.	Verifies token exists & not expired/revoked
	2.	Issues new pair (access + refresh)
	3.	Marks old refresh as revoked_at=now.
	•	Add logout to revoke all user refresh tokens.
	•	Tests: refresh flow, revoked token fails.

⸻

3 — OAuth Hardening

3.1 Add CSRF state parameter (and PKCE for Google)

Why Protects against CSRF/login CSRF attacks.
What
	•	When generating auth URL, create crypto‑random 32‑byte string → store in server‑side session or Redis keyed by nonce cookie.
	•	Validate state on callback before exchanging code.
	•	For Google: implement PKCE (code_challenge/code_verifier) path.
Hints oauthlib examples; fall back to S256.

⸻

3.2 Verify Google id_token and GitHub email verification

Why Ensure email ownership.
What
	•	After token exchange, call Google’s tokeninfo endpoint or use google‑auth lib to validate signature & aud.
	•	Accept user only if email_verified is true.
	•	GitHub: choose first {"primary":true,"verified":true} email; else fail.

⸻

4 — Password & Account Lifecycle

4.1 Centralize password complexity validation

Why Avoid duplicated regex logic.
What
	•	Move regex checks into users/utils.validate_password_complexity().
	•	Import in both UserCreate & PasswordResetConfirm validators.

⸻

4.2 Make is_token_expired() null‑safe

Why Prevent TypeError if DB column is NULL.
What

if expires_at is None: return True
return utcnow() > expires_at



⸻

4.3 Return generic messages for verify/reset endpoints

Why Stop token‑guess enumeration.
What
	•	/verify-email, /reset-password should always return 200 + generic text, even for invalid/expired tokens.
	•	Internally log success/failure with logger.info.

⸻

5 — Mail Delivery

5.1 Make email sending non‑blocking

Why async function uses blocking smtplib → stalls event loop.
What
	•	Option A: mark _send_email sync and wrap with run_in_threadpool (fastapi.concurrency).
	•	Option B: switch to aiosmtplib.
	•	Stress‑test: send 30 mails concurrently and ensure response < 500 ms.

⸻

6 — API UX & Security

6.1 Change‑password endpoint to use JSON body

Why Current query params leak secrets in logs.
What
	•	Create ChangePassword Pydantic model.
	•	Update route to @router.post("/change-password") receiving body.
	•	Update docs & frontend.

⸻

6.2 Optional: deliver tokens in Http‑Only cookies

Why Reduce XSS exposure when SPA served from same site.
What
	•	If settings.AUTH_COOKIES=true, FastAPI sets Set-Cookie for access_token (max‑age = TTL, HttpOnly, Secure, SameSite=Lax).
	•	Add middleware to read cookie and populate Authorization header for backend endpoints (or change FE fetch).
	•	Provide fallback to current Bearer header for public APIs.

⸻

7 — Tests & CI

7.1 Add pytest‑asyncio suite for auth flows

Why Regression safety.
What
	•	Spin up test DB via sqlmodel.create_engine("sqlite:///:memory:").
	•	Cover: register → verify → login → refresh → change‑password → password‑reset → RBAC.
	•	Minimum coverage target 85 % on backend/services/users/*.

⸻

8 — Observability

8.1 Implement structured audit logs

Why Track security‑relevant events.
What
	•	Use structlog with JSON renderer.
	•	Emit on: login success/fail, logout, password reset request, email verify.
	•	Include user_id, ip, ua, event.
	•	Expose /metrics Prometheus counter for auth failures.

⸻

9 — Dev & Ops

9.1 Load secrets via environment / Docker secrets

Why Avoid putting secrets into baked images.
What
	•	Docs: instruct using docker secret or Kubernetes Secrets.
	•	Remove defaults for SMTP_USERNAME/PASSWORD, JWT_SECRET_KEY in settings.py; raise RuntimeError if missing in prod.

9.2 Rate‑limit sensitive endpoints

Why Brute‑force & spam mitigation.
What
	•	Integrate slowapi or API‑gateway limiter.
	•	5 req/min for /auth/login, /auth/request-password-reset.
	•	Tests: 6th request returns 429.

⸻

10 — Misc Quality Nits

10.1 Rename LoginCredentials.username → login

Why Reflects “username or email”.
What
	•	Update schema & FE calls (authService.login).
	•	Deprecate old field until FE updated.

10.2 Extract EMAIL_REGEX constant

Why DRY.
What
	•	Place in users/utils.py → import in validators.

10.3 Use secrets.token_urlsafe() for URL tokens

Why Guarantees URL‑safe characters.
What
	•	Replace generate_random_token() implementation accordingly.

⸻

How to work these tasks
	1.	Prioritise security items (2, 3, 4, 5) for immediate sprint.
	2.	Create branches per top‑level section; keep migrations sequential.
	3.	After every section, bump template version + run test suite.

Feel free to pass this backlog verbatim to the AI developer or slice it into sprint‑sized chunks (✅ symbols are great for tracking progress).