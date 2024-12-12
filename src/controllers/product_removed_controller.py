from src.models.product_removed_model import ProductRemovedModel
from src.views.addons_view import AddonsView
from src.views.product_view import ProductView

product_removed_model = ProductRemovedModel()
product_view = ProductView()
addons_view = AddonsView()
class ProductRemovedController:

    def list_products_removed(self):        
        products = product_removed_model.read_all_products_removed()
        if products:
            product_view.show_products(products, 'Productos Eliminados')
        else:
            addons_view.clear_screen()
            addons_view.show_report_menu()
            addons_view.show_message('No se encontraron PRODUCTOS ELIMINADOS.')

