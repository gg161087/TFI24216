from src.views.menu_view import MenuView
from src.data.db_connection import initialize_db
from src.data.seed import seeder      

menu_view = MenuView()

if __name__ == "__main__":
    # Inicializa la tabla para Productos, indicando que la columna code(Código) es unica
    initialize_db('products', 'UNIQUE')
    # Inicializa la tabla para Productos Eliminados, aca si puede haber varios productos con el mismo código
    initialize_db('products_removed', '')
    # Agrega productos en modo ejemplo para poder probar el programa, COMENTAR para que no agregue datos.
    seeder()    
    menu_view.main_menu()
