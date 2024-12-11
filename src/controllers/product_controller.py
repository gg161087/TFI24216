from src.models.product_model import ProductModel
from src.views.product_view import ProductView

class ProductController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def create_product(self):
        try:
            code = int(self.view.get_input("Ingrese el código del producto: "))
            name = self.view.get_input("Ingrese el nombre del producto: ")
            price = float(self.view.get_input("Ingrese el precio del producto: "))
            stock = int(self.view.get_input("Ingrese el stock del producto: "))
            self.model.create_product(code, name, price, stock)
            self.view.display_message("Producto creado exitosamente.")
        except ValueError:
            self.view.display_message("Error: Entrada inválida. Intente nuevamente.")

    def list_products(self):
        products = self.model.read_all_products()
        self.view.display_products(products)

    def update_product(self):
        try:
            product_id = int(self.view.get_input("Ingrese el ID del producto a actualizar: "))
            code = int(self.view.get_input("Ingrese el nuevo código del producto: "))
            name = self.view.get_input("Ingrese el nuevo nombre del producto: ")
            price = float(self.view.get_input("Ingrese el nuevo precio del producto: "))
            stock = int(self.view.get_input("Ingrese el nuevo stock del producto: "))
            self.model.update_product(product_id, code, name, price, stock)
            self.view.display_message("Producto actualizado exitosamente.")
        except ValueError:
            self.view.display_message("Error: Entrada inválida. Intente nuevamente.")

    def delete_product(self):
        try:
            product_id = int(self.view.get_input("Ingrese el ID del producto a eliminar: "))
            self.model.delete_product(product_id)
            self.view.display_message("Producto eliminado exitosamente.")
        except ValueError:
            self.view.display_message("Error: Entrada inválida. Intente nuevamente.")
