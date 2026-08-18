"""
SCHEMA
------
A Schema describes the JSON shape of API requests and responses.
Pydantic checks types automatically (e.g. price must be a number).

Teaching point:
  Model  = database table (SQLAlchemy)
  Schema = API JSON contract (Pydantic)

Why three schemas?
  ProductCreate   - what the client sends to ADD a product (no id yet)
  ProductUpdate   - what the client sends to UPDATE a product
  ProductResponse - what the API returns (includes id from the database)
"""

from pydantic import BaseModel, Field


class ProductCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=120, examples=["Wireless Mouse"])
    description: str | None = Field(default=None, max_length=500)
    price: float = Field(..., gt=0, examples=[799.0])
    quantity: int = Field(..., ge=0, examples=[25])


class ProductUpdate(BaseModel):
    name: str = Field(..., min_length=1, max_length=120)
    description: str | None = Field(default=None, max_length=500)
    price: float = Field(..., gt=0)
    quantity: int = Field(..., ge=0)


class ProductResponse(BaseModel):
    id: int
    name: str
    description: str | None
    price: float
    quantity: int

    class Config:
        from_attributes = True  # allows converting SQLAlchemy model -> JSON
