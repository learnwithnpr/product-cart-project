from app.database import get_connection
from app.schemas.product import Product


class ProductService:
    def get_all_products(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM products")
        products = cursor.fetchall()

        cursor.close()
        conn.close()
        return products

    def create_product(self, product: Product):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO products (name, price, quantity)
            VALUES (%s, %s, %s)
            RETURNING *
            """,
            (product.name, product.price, product.quantity)
        )

        new_product = cursor.fetchone()
        conn.commit()

        cursor.close()
        conn.close()
        return new_product

    def update_product(self, product_id: int, product: Product):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE products
            SET name = %s, price = %s, quantity = %s
            WHERE id = %s
            RETURNING *
            """,
            (product.name, product.price, product.quantity, product_id)
        )

        updated_product = cursor.fetchone()
        conn.commit()

        cursor.close()
        conn.close()
        return updated_product

    def delete_product(self, product_id: int):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM products WHERE id = %s", (product_id,))
        conn.commit()

        cursor.close()
        conn.close()
        return {"message": "Product deleted successfully"}
