"""
DATABASE
--------
Creates the PostgreSQL connection and a session for each request.

Teaching points:
  - engine     = the actual connection to Postgres
  - Session    = one unit of work (read/write) with the database
  - get_db()   = FastAPI dependency: open session, use it, then close it
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from app.config import settings

engine = create_engine(settings.DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# All SQLAlchemy models inherit from this Base class.
Base = declarative_base()


def get_db():
    """Provide a database session, then always close it."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
