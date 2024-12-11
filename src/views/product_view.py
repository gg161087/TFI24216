import os
from colorama import Fore, Back, init
from src.views.addons_view import AddonsView

addons_view = AddonsView()

class ProductView:
    def __init__(self):
        # Inicializa colorama con autoreset
        init(autoreset=True)

    def display_table_headers(self):
        print(f'\t{Back.GREEN}{"#":<5}{"Código":<12}{"Producto":<15}{"Precio($)":>15}{"Stock":>15}')

    def display_product(self, product):    
        print(f'\t{product['id']:<5}{product['code']:<12}{product['name']:<15}{product['price']:>15.2f}{product['stock']:>15}')

    def table_products(self, title, options, paginated, current_page, products, total_pages): 
        addons_view.clear_screen()        
        addons_view.display_title_menu(title, options, 'letra')
        addons_view.display_back_menu()
        self.display_table_headers()       
        for product in paginated[current_page]:
            self.display_product(product)
        addons_view.display_divider()
        print(f'\tProductos Total: {len(products)}') 
        if total_pages > 1:
            addons_view.display_paginated_controls(current_page, total_pages)
        else:
            addons_view.display_divider()

    def display_products(self, products, title, page_size=5):
    # Muestra los productos en forma paginada en la consola. 
        back = False 
        paginated = list(addons_view.paginate_list(products, page_size))
        total_pages = len(paginated)
        options = ''
        if total_pages > 1:
            options = 'S-A-V'
        else:
            options = 'V'
        current_page = 0     
        self.table_products(title, options, paginated, current_page, products, total_pages)
        while not back:
            choice = input('\tSeleccione una opción: ').strip().lower()            
            if choice.lower() == 's':                        
                if current_page < total_pages - 1:                
                    current_page += 1
                    self.table_products(title, options, paginated, current_page, products, total_pages)
                else:
                    self.table_products(title, options, paginated, current_page, products, total_pages)                                               
                    print('\tYa estás en la última página.')
                    addons_view.display_divider()
            elif choice.lower() == 'a':                        
                if current_page > 0:                
                    current_page -= 1
                    self.table_products(title, options, paginated, current_page, products, total_pages)
                else: 
                    self.table_products(title, options, paginated, current_page, products, total_pages)                             
                    print('\tYa estás en la primera página.')
                    addons_view.display_divider()
            elif choice.lower() == 'v':
                back = True
                addons_view.clear_screen()  
                addons_view.display_menu()         
                break
            else:            
                self.table_products(title, options, paginated, current_page, products, total_pages)            
                addons_view.display_invalid_option(top_divider=False)          

    def display_product_requirements(self):    
        print(f'El código debe ser numérico y de 4 cifras, \nEl nombre debe tener al menos 3 caracteres, \nEl stock numérico mayor o igual a 0 y \nEl precio numérico/mayor que 0.')
        addons_view.display_divider() 