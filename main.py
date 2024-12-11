from src.views.main_menu import main_menu
from src.data.db_connection import initialize_db
from src.data.seed import seeder      

if __name__ == "__main__":
    initialize_db('products', 'UNIQUE')
    initialize_db('products_removed', '')
    seeder()
    main_menu()
