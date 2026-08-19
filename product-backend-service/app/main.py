"""
MAIN
----
This is the application entry point.

Run:
  uvicorn app.main:app --reload

Teaching flow:
  Request from React UI
    -> Controller (HTTP)
    -> Service (business logic)
    -> Model (database table)
    -> PostgreSQL
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy import inspect, text

from app.database import Base, engine
from app.controllers import product_router
from app import models  # noqa: F401  # import models so SQLAlchemy creates tables

# Create tables if they do not exist yet.
# create_all() will not add new columns to an old table.
Base.metadata.create_all(bind=engine)

# The demo table may already exist without description. Add it if missing.
inspector = inspect(engine)
if inspector.has_table("products"):
    column_names = [column["name"] for column in inspector.get_columns("products")]
    if "description" not in column_names:
        with engine.begin() as connection:
            connection.execute(text("ALTER TABLE products ADD COLUMN description VARCHAR(500)"))

app = FastAPI(
    title="Product Backend Service",
    description="Student demo: Product CRUD with FastAPI + PostgreSQL",
    version="1.0.0",
)

# Allow the React app (Vite default port 5173) to call this API.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(product_router)


@app.get("/")
def health():
    return {"status": "ok", "service": "product-backend-service"}
