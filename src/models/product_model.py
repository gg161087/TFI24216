import sqlite3
from src.data.db_connection import get_connection

class ProductModel:
    def create_product(self, code, name, price, stock):
        query = 'INSERT INTO products (code, name, price, stock) VALUES (?, ?, ?, ?)'
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(query, (code, name, price, stock))
            conn.commit()
            # Devuelve el ID del nuevo producto
            return cursor.lastrowid 
        # Manejo de errores
        except sqlite3.Error as e:
            print(f'Error al crear producto: {e}')
            return None 
        except sqlite3.IntegrityError as e:
            print(f'Error al crear producto: El código: {code}, ya existe. Detalles: {e}')
            return None
        # Cerrar connexion y verifica si `conn` fue inicializado
        finally:
            if conn:
                conn.close()

    def read_all_products(self):
        query = f'SELECT * FROM products'   
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(query)
            results = cursor.fetchall()
            conn.close()
            keys = ['id', 'code', 'name', 'price', 'stock']
            dict_results = [dict(zip(keys, row)) for row in results]
            return dict_results
        except sqlite3.Error as e:
            print(f'Error al obtener los productos: {e}')
            return None
        finally:
            if conn:
                conn.close()

    def read_product_dynamic(self, condition, parameter):
        query = f'SELECT * FROM products WHERE {condition} = ?'
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(query, (parameter,))    
            row = cursor.fetchone()   
            if row:        
                return {
                    "id": row[0],
                    "code": row[1],
                    "name": row[2],
                    "price": row[3],
                    "stock": row[4],
                }
        except sqlite3.Error as e:
            print(f'Error al obtener el producto: {e}')
            return None    
        finally:
            if conn:
                conn.close()

    def update_product(self, id, code, name, price, stock):
        query = """
            UPDATE products
            SET code = ?, name = ?, price = ?, stock = ?
            WHERE id = ?
        """
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(query, (code, name, price, stock, id))
            conn.commit()
            updated_rows = cursor.rowcount
            conn.close()
            return updated_rows > 0
        except sqlite3.Error as e: 
            print(f'Error al actualizar el producto con ID {id}: {e}')
            return False
        finally:
            if conn:
                conn.close() 

    def delete_product(self, id):
        query_check = 'SELECT 1 FROM products WHERE id = ?'
        query_delete = 'DELETE FROM products WHERE id = ?'
        conn = get_connection()
        cursor = conn.cursor()
        try:
            # Verificar si el producto existe
            cursor.execute(query_check, (id,))
            product_exists = cursor.fetchone()
            # El producto existe, proceder con la eliminación
            if product_exists:
                cursor.execute(query_delete, (id,))
                conn.commit()
                return True
            else:                
                return False
        except sqlite3.Error as e:
            print(f'Error al intentar eliminar el producto con ID {id}: {e}')
            return False
        finally:
            if conn:
                conn.close()

    def read_low_stock_products(self):
        query = 'SELECT * FROM products WHERE stock <= 10'
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(query)
            results = cursor.fetchall()
            keys = ['id', 'code','name', 'price', 'stock']
            dict_results = [dict(zip(keys, row)) for row in results]
            return dict_results
        except sqlite3.Error as e:
            print(f'Error al obtener los productos con bajo stock: {e}')
            return None
        finally:
            if conn:  
                conn.close() 