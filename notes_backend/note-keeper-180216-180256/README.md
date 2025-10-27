# note-keeper-180216-180256

Backend: Django REST API for Notes CRUD

Base URL (preview): /api

Endpoints:
- GET /api/health/ -> health check
- GET /api/notes/ -> list notes (paginated)
- POST /api/notes/ -> create note
- GET /api/notes/{id}/ -> retrieve note
- PUT /api/notes/{id}/ -> update note
- PATCH /api/notes/{id}/ -> partial update note
- DELETE /api/notes/{id}/ -> delete note

Example usage (replace BASE with your preview base URL):
- List: curl -s "$BASE/api/notes/"
- Create: curl -s -X POST "$BASE/api/notes/" -H "Content-Type: application/json" -d '{"title":"First","content":"Hello"}'
- Retrieve: curl -s "$BASE/api/notes/{id}/"
- Update: curl -s -X PUT "$BASE/api/notes/{id}/" -H "Content-Type: application/json" -d '{"title":"Updated","content":"World"}'
- Delete: curl -s -X DELETE "$BASE/api/notes/{id}/"

Notes:
- CORS is enabled for development (CORS_ALLOW_ALL_ORIGINS=True). Tighten for production.
- Pagination defaults to 10 per page; override via ?page_size=XX (max 100).
- No hard-coded secrets should be used in production; use environment variables. If introducing new env vars, update .env.example accordingly.
