from src.models.product_model import ProductModel
from src.views.product_view import ProductView
from src.controllers.product_controller import ProductController

def main_menu():
    model = ProductModel()
    view = ProductView()
    controller = ProductController(model, view)
    while True:
        print("\n--- Menú de Productos ---")
        print("1. Listar productos")
        print("2. Crear producto")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Salir")
        choice = view.get_input("Seleccione una opción: ")

        if choice == "1":
            controller.list_products()
        elif choice == "2":
            controller.create_product()
        elif choice == "3":
            controller.update_product()
        elif choice == "4":
            controller.delete_product()
        elif choice == "5":
            print("¡Adiós!")
            break
        else:
            view.display_message("Opción no válida. Intente nuevamente.")