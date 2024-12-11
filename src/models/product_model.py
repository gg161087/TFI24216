from src.data.db_connection import get_connection

class ProductModel:
    def create_product(self, code, name, price, stock):
        conn = get_connection()
        cursor = conn.cursor()
        query = "INSERT INTO products (code, name, price, stock) VALUES (?, ?, ?, ?)"
        cursor.execute(query, (code, name, price, stock))
        conn.commit()
        conn.close()

    def read_all_products(self):
        conn = get_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM products"
        products = cursor.execute(query).fetchall()
        conn.close()
        return products

    def update_product(self, product_id, code, name, price, stock):
        conn = get_connection()
        cursor = conn.cursor()
        query = """
        UPDATE products 
        SET code = ?, name = ?, price = ?, stock = ?
        WHERE id = ?
        """
        cursor.execute(query, (code, name, price, stock, product_id))
        conn.commit()
        conn.close()

    def delete_product(self, product_id):
        conn = get_connection()
        cursor = conn.cursor()
        query = "DELETE FROM products WHERE id = ?"
        cursor.execute(query, (product_id,))
        conn.commit()
        conn.close()
