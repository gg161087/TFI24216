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
        addons_view.clear_screen()
        addons_view.show_main_menu()
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
                    self.update_product_menu()                
                case '5':
                    addons_view.clear_screen()
                    self.report_product_menu()
                case '6':
                    addons_view.clear_screen()
                    self.remove_product_menu()
                case '7':
                    addons_view.show_closing_program()
                    break
                case _:
                    addons_view.clear_screen()
                    addons_view.show_main_menu()
                    addons_view.show_invalid_option()            

    def search_product_menu(self):
        addons_view.clear_screen()
        addons_view.show_dynamic_menu('BUSCAR')
        while True:                    
            prompt = input('\t Seleccione una opción: ').strip()
            match prompt:
                case '1':
                    addons_view.clear_screen()
                    product_controller.dynamic_product_controller('buscar', 'id')
                    #product_controller.search_product_controller('ID')                                       
                case '2':
                    addons_view.clear_screen()
                    product_controller.dynamic_product_controller('buscar', 'código')
                    #product_controller.search_product_controller('CÓDIGO') 
                case '3':  
                    addons_view.clear_screen()
                    product_controller.dynamic_product_controller('buscar', 'nombre')
                    #product_controller.search_product_controller('NOMBRE')
                case '4':
                    addons_view.clear_screen()
                    addons_view.show_main_menu()                                      
                    break
                case _:
                    addons_view.clear_screen()
                    addons_view.show_dynamic_menu('BUSCAR')                    
                    addons_view.show_invalid_option() 
            
    def update_product_menu(self):
        addons_view.clear_screen()
        addons_view.show_dynamic_menu('ACTUALIZAR')
        while True:        
            prompt = input('\t Seleccione una opción: ')
            match prompt:
                case '1':
                    addons_view.clear_screen()
                    product_controller.dynamic_product_controller('actualizar', 'id')
                    #product_controller.update_product_controller('ID')                   
                case '2':
                    addons_view.clear_screen()
                    product_controller.dynamic_product_controller('actualizar', 'código')
                    #product_controller.update_product_controller('CÓDIGO')
                case '3':  
                    addons_view.clear_screen()
                    product_controller.dynamic_product_controller('actualizar', 'nombre')
                    #product_controller.update_product_controller('NOMBRE')
                case '4':
                    addons_view.clear_screen() 
                    addons_view.show_main_menu()                                           
                    break
                case _:
                    addons_view.clear_screen()
                    addons_view.show_dynamic_menu('ACTUALIZAR')
                    addons_view.show_invalid_option() 

    def report_product_menu(self):
        addons_view.clear_screen()
        addons_view.show_report_menu()
        while True:
            prompt = input('\t Seleccione una opción: ')
            match prompt:
                case '1':
                    addons_view.clear_screen()
                    product_controller.low_stock_report_controller()
                case '2':
                    addons_view.clear_screen()
                    product_removed_controller.list_products_removed()
                case '3':
                    addons_view.clear_screen()
                    addons_view.show_main_menu()                    
                    break
                case _:
                    addons_view.clear_screen()
                    addons_view.show_report_menu()
                    addons_view.show_invalid_option() 

    def remove_product_menu(self):
        addons_view.clear_screen()    
        addons_view.show_dynamic_menu('ELIMINAR')
        while True:
            prompt = input('\t Seleccione una opción: ')
            match prompt:
                case '1':
                    addons_view.clear_screen()
                    product_controller.dynamic_product_controller('eliminar', 'id')                
                case '2':
                    addons_view.clear_screen()
                    product_controller.dynamic_product_controller('eliminar', 'código')
                case '3':  
                    addons_view.clear_screen()
                    product_controller.dynamic_product_controller('eliminar', 'nombre')
                case '4':#
                    addons_view.clear_screen()
                    addons_view.show_main_menu()                                           
                    break
                case _:
                    addons_view.clear_screen()
                    addons_view.show_dynamic_menu('ELIMINAR')
                    addons_view.show_invalid_option()
 