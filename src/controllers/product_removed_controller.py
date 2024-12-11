from src.models.product_removed_model import ProductRemovedModel
from src.views.product_view import ProductView

product_removed_model = ProductRemovedModel()
product_view = ProductView()

class ProductRemovedController:
    def create_product_removed(self):
        try:
            code = int(self.view.get_input("Ingrese el código del producto: "))
            name = self.view.get_input("Ingrese el nombre del producto: ")
            price = float(self.view.get_input("Ingrese el precio del producto: "))
            stock = int(self.view.get_input("Ingrese el stock del producto: "))
            self.model.create_product(code, name, price, stock)
            self.view.display_message("Producto creado exitosamente.")
        except ValueError:
            self.view.display_message("Error: Entrada inválida. Intente nuevamente.")

    def list_products_removed(self):
        products = self.model.read_all_products()
        self.view.display_products(products, 'Productos Eliminados')

    def update_product_removed(self):
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

    def delete_product_removed(self):
        try:
            product_id = int(self.view.get_input("Ingrese el ID del producto a eliminar: "))
            self.model.delete_product(product_id)
            self.view.display_message("Producto eliminado exitosamente.")
        except ValueError:
            self.view.display_message("Error: Entrada inválida. Intente nuevamente.")
