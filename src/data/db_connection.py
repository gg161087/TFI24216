import os
import sqlite3

PRODUCTS = os.path.join(os.path.dirname(__file__), 'PRODUCTS.db')

def get_connection():
    return sqlite3.connect(PRODUCTS)

def initialize_db(table_name, parameter):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            code INTEGER NOT NULL {parameter},
            name TEXT NOT NULL,
            price REAL NOT NULL,
            stock INTEGER NOT NULL
        )
    """
    )
    conn.commit()
    conn.close()