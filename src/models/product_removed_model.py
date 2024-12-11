from src.data.db_connection import get_connection

class ProductRemovedModel:
    def create_product_removed(self, code, name, price, stock):
        conn = get_connection()
        cursor = conn.cursor()
        query = "INSERT INTO products_removed (code, name, price, stock) VALUES (?, ?, ?, ?)"
        cursor.execute(query, (code, name, price, stock))
        conn.commit()
        conn.close()

    def read_all_products_removed(self):
        conn = get_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM products_removed"
        products = cursor.execute(query).fetchall()
        conn.close()
        return products

    def update_product_removed(self, product_id, code, name, price, stock):
        conn = get_connection()
        cursor = conn.cursor()
        query = """
        UPDATE products_removed 
        SET code = ?, name = ?, price = ?, stock = ?
        WHERE id = ?
        """
        cursor.execute(query, (code, name, price, stock, product_id))
        conn.commit()
        conn.close()

    def delete_product_removed(self, product_id):
        conn = get_connection()
        cursor = conn.cursor()
        query = "DELETE FROM products_removed WHERE id = ?"
        cursor.execute(query, (product_id,))
        conn.commit()
        conn.close()
