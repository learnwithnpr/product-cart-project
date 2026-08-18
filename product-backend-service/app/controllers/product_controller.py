"""
CONTROLLER
----------
A Controller maps HTTP URLs to service methods.

Teaching point:
  GET    /products      -> list products
  POST   /products      -> add a product
  GET    /products/{id} -> get one product
  PUT    /products/{id} -> update a product
  DELETE /products/{id} -> delete a product
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.product import ProductCreate, ProductUpdate, ProductResponse
from app.services.product_service import ProductService

router = APIRouter(tags=["Products"])


def get_product_service(db: Session = Depends(get_db)) -> ProductService:
    return ProductService(db)


@router.get("/products", response_model=list[ProductResponse])
def list_products(service: ProductService = Depends(get_product_service)):
    return service.get_all_products()


@router.get("/products/{product_id}", response_model=ProductResponse)
def get_product(product_id: int, service: ProductService = Depends(get_product_service)):
    product = service.get_product(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.post("/products", response_model=ProductResponse, status_code=201)
def create_product(
    data: ProductCreate,
    service: ProductService = Depends(get_product_service),
):
    return service.create_product(data)


@router.put("/products/{product_id}", response_model=ProductResponse)
def update_product(
    product_id: int,
    data: ProductUpdate,
    service: ProductService = Depends(get_product_service),
):
    updated = service.update_product(product_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated


@router.delete("/products/{product_id}")
def delete_product(product_id: int, service: ProductService = Depends(get_product_service)):
    deleted = service.delete_product(product_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted successfully"}
