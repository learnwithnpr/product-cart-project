"""
CONFIG
------
Reads settings from environment variables / .env file.

Teaching point:
  Do not hard-code database passwords in Python files.
  Keep them in .env (local) and load them here.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str = (
        "postgresql+psycopg2://postgres:postgres@localhost:5432/product_db"
    )

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
