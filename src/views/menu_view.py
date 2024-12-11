from src.controllers.product_controller import ProductController
from src.controllers.product_removed_controller import ProductRemovedController
from src.models.product_model import ProductModel
from src.models.product_removed_model import ProductRemovedModel
from src.views.addons_view import AddonsView

product_model = ProductModel()
product_removed_model = ProductRemovedModel()
addons_view = AddonsView()
product_controller = ProductController()
product_removed_controller = ProductRemovedController()

class MenuView:
    def main_menu(self):
        addons_view.display_menu()
        while True:       
            prompt = input('\t Seleccione una opción: ').strip()
            match prompt:
                case '1':
                    addons_view.clear_screen()
                    product_controller.create_product()                
                case '2':
                    addons_view.clear_screen()
                    product_controller.list_products()                
                case '3':  
                    addons_view.clear_screen()                                  
                    self.search_product_menu()
                case '4':
                    addons_view.clear_screen()
                    product_controller.update_product()                
                case '5':
                    addons_view.clear_screen()
                    self.report_product_menu()
                case '6':
                    addons_view.clear_screen()
                    self.remove_product_menu()
                case '7':
                    addons_view.display_closing_program()
                    break
                case _:
                    addons_view.clear_screen()
                    addons_view.display_menu()
                    addons_view.display_invalid_option() 

    def search_product_menu(self):
        while True:        
            addons_view.display_dynamic_selector('Buscar')
            prompt = input('\t Seleccione una opción: ').strip()
            match prompt:
                case '1':
                    addons_view.clear_screen()
                    product_controller.search_product_dynamic('ID')
                    # search_product_controller('ID')                     
                case '2':
                    addons_view.clear_screen()
                    product_controller.search_product_dynamic('CÓDIGO') 
                case '3':  
                    addons_view.clear_screen()
                    product_controller.search_product_dynamic('NOMBRE')
                case '4':
                    addons_view.clear_screen()
                    addons_view.display_menu()                  
                    break
                case _:
                    addons_view.clear_screen()
                    addons_view.display_invalid_option() 

    def update_product_menu(self):
        while True:        
            addons_view.display_dynamic_selector('Buscar y Actualizar')
            prompt = input('\t Seleccione una opción: ')
            match prompt:
                case '1':
                    addons_view.clear_screen()
                    # Update_controller ID                   
                case '2':
                    addons_view.clear_screen()
                    # Update_controller CODIGO
                case '3':  
                    addons_view.clear_screen()
                    # Update_controller NOMBRE
                case '4':
                    addons_view.clear_screen()
                    addons_view.display_menu()                        
                    break
                case _:
                    addons_view.clear_screen()
                    addons_view.display_invalid_option() 

    def report_product_menu(self):
        while True:
            addons_view.display_report_menu()
            prompt = input('\t Seleccione una opción: ')
            match prompt:
                case '1':
                    addons_view.clear_screen()
                    # Low stock report Controller
                case '2':
                    addons_view.clear_screen()
                    # List products removed
                case '3':
                    addons_view.clear_screen()
                    addons_view.display_menu()
                    break
                case _:
                    addons_view.clear_screen()
                    addons_view.display_invalid_option() 

    def remove_product_menu(self):    
        while True:
            addons_view.display_dynamic_selector('Eliminar')
            prompt = input('\t Seleccione una opción: ')
            match prompt:
                case '1':
                    addons_view.clear_screen()
                    # Remove_controller ID                   
                case '2':
                    addons_view.clear_screen()
                    # Remove_controller CODIGO
                case '3':  
                    addons_view.clear_screen()
                    # Remove_controller NOMBRE
                case '4':
                    addons_view.clear_screen()
                    addons_view.display_menu()                        
                    break
                case _:
                    addons_view.clear_screen()
                    addons_view.display_invalid_option()
 