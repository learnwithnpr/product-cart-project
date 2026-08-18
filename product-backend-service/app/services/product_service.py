"""
SERVICE
-------
A Service contains BUSINESS LOGIC and talks to the database.

Teaching point:
  Controllers should stay thin (HTTP only).
  Services do the real work: create, read, update, delete.
"""

from sqlalchemy.orm import Session

from app.models.product import Product
from app.schemas.product import ProductCreate, ProductUpdate


class ProductService:
    def __init__(self, db: Session):
        self.db = db

    def create_product(self, data: ProductCreate) -> Product:
        product = Product(
            name=data.name,
            description=data.description,
            price=data.price,
            quantity=data.quantity,
        )
        self.db.add(product)
        self.db.commit()
        self.db.refresh(product)  # load the generated id
        return product

    def get_all_products(self) -> list[Product]:
        return self.db.query(Product).order_by(Product.id.desc()).all()

    def get_product(self, product_id: int) -> Product | None:
        return self.db.query(Product).filter(Product.id == product_id).first()

    def update_product(self, product_id: int, data: ProductUpdate) -> Product | None:
        product = self.get_product(product_id)
        if not product:
            return None

        product.name = data.name
        product.description = data.description
        product.price = data.price
        product.quantity = data.quantity

        self.db.commit()
        self.db.refresh(product)
        return product

    def delete_product(self, product_id: int) -> Product | None:
        product = self.get_product(product_id)
        if not product:
            return None

        self.db.delete(product)
        self.db.commit()
        return product
