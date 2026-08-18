"""
MODEL
-----
A Model is a Python class that maps to a DATABASE TABLE.

Teaching point:
  Product (this file)  -->  table named "products" in PostgreSQL
  Each class attribute -->  one column in that table
"""

from sqlalchemy import Column, Integer, String, Float

from app.database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(120), nullable=False)
    description = Column(String(500), nullable=True)
    price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False, default=0)
