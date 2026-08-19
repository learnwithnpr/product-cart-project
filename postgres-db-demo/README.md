# postgres-db-demo

Simple FastAPI Product CRUD using PostgreSQL cursor SQL.

Folder notes PDF: `notes/FastAPI-Product-API-Guide.pdf`

## Run

```bash
cd postgres-db-demo
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Docs: http://localhost:8000/docs

Edit `app/database.py` if the Postgres username or password is different.
