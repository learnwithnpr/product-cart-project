# Product Card Manager (Student Project)

Two projects that work together:

1. `product-backend-service` — FastAPI + PostgreSQL APIs
2. `product-ui-app` — React UI for product cards

```
React UI  -->  FastAPI  -->  PostgreSQL
```

## How to run

PostgreSQL should already be installed and running.

Create a database named `product_db` (pgAdmin or psql):

```sql
CREATE DATABASE product_db;
```

### 1. Start the backend

```bash
cd product-backend-service
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Open `.env` and put your Postgres username and password.

Then start the API:

```bash
uvicorn app.main:app --reload
```

API docs: http://localhost:8000/docs

### 2. Start the UI

Open a new terminal:

```bash
cd product-ui-app
npm install
npm run dev
```

UI: http://localhost:5173

## Classroom concepts

| Layer | Folder | Job |
|-------|--------|-----|
| Controller | `app/controllers` | HTTP URLs |
| Schema | `app/schemas` | JSON validation |
| Service | `app/services` | Create / Read / Update / Delete |
| Model | `app/models` | Database table |
| Database | PostgreSQL | Stores products |
| UI | `product-ui-app` | Product cards and forms |
