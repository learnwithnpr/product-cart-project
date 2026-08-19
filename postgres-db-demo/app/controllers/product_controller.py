from fastapi import APIRouter, Depends

from app.schemas.product import Product
from app.services.product_service import ProductService

router = APIRouter()


def get_product_service() -> ProductService:
    return ProductService()


@router.get("/products")
def get_products(service: ProductService = Depends(get_product_service)):
    return service.get_all_products()


@router.post("/products")
def create_product(product: Product, service: ProductService = Depends(get_product_service)):
    return service.create_product(product)


@router.put("/products/{product_id}")
def update_product(
    product_id: int,
    product: Product,
    service: ProductService = Depends(get_product_service),
):
    return service.update_product(product_id, product)


@router.delete("/products/{product_id}")
def delete_product(product_id: int, service: ProductService = Depends(get_product_service)):
    return service.delete_product(product_id)
