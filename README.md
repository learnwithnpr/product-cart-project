# Product Card Manager

Product CRUD demo with FastAPI + React.

## Projects

1. `product-backend-service` — FastAPI + PostgreSQL (SQLAlchemy)
2. `product-ui-app` — React product card UI

```
React UI (:5173)  -->  FastAPI (:8000)  -->  PostgreSQL
```

## Other course repos (separate)

- https://github.com/learnwithnpr/postgres-db-demo
- https://github.com/learnwithnpr/ai-chat-service
- https://github.com/learnwithnpr/ai-chat-ui

## How to run

### Backend

```bash
cd product-backend-service
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# edit .env with your Postgres password
uvicorn app.main:app --reload
```

Docs: http://localhost:8000/docs

### UI

Install Node.js LTS from https://nodejs.org first.

```bash
cd product-ui-app
npm install
npm run dev
```

UI: http://localhost:5173
