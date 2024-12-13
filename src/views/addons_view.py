import os
from colorama import Fore, Back, init

class AddonsView:
    def __init__(self):
        # Inicializa colorama con autoreset
        init(autoreset=True) 

    def clear_screen(self):
        # Limpia la consola según el sistema operativo.        
        os.system('cls' if os.name == 'nt' else 'clear') 

    def show_divider(self): 
        # Muestra un divisor decorativo.       
        print(Fore.YELLOW + '-' * 78) 

    def show_title_menu_dynamic(self, title, options, input_type='número'):
        # Muestra el título y las opciones de un menú.
        title = title.upper()
        self.show_divider()
        print(f'Menú {Back.GREEN}{Fore.BLACK} {title} {Back.RESET}{Fore.RESET}, Escriba {input_type} de opción ({Fore.YELLOW}{options}{Fore.RESET}):'.center(50))
        self.show_divider()

    def show_title_menu(self, title):
        # Muestra el título y las opciones de un menú.
        title = title.upper()
        self.show_divider()        
        print(f'Menú {Back.GREEN}{Fore.BLACK} {title} {Back.RESET}{Fore.RESET}, Escriba la letra ({Fore.YELLOW}V{Fore.RESET}) para volver:'.center(50))
        self.show_divider()

    def show_confirm(self, action):
        # Muestra un mensaje de confirmación para una acción específica.
        action = action.upper()
        self.show_divider()
        print(f'Desea {action}: [{Fore.YELLOW}S{Fore.RESET}] Si | [{Fore.YELLOW}N{Fore.RESET}] No')
        self.show_divider()
    
    def show_message(self, message):
        self.show_divider()
        print(message)
        self.show_divider()

    def show_invalid_data(self):
        self.show_divider()
        print('Datos ingresados incorrectos, intente de nuevo.')
        self.show_divider()

    def show_invalid_option(self, top_divider=True):
        # Muestra un mensaje de opción inválida.
        if top_divider:
            self.show_divider()
        print('\tOpción no válida, intente de nuevo.')
        self.show_divider()
    
    def show_invalid_id(self):
        # Muestra un mensaje de requisitos de id.    
        self.show_divider()
        print('El ID del producto debe ser numerico y mayor que 0.')
        self.show_divider()
    
    def show_invalid_code(self):
        # Muestra un mensaje de requisitos de code.
        self.show_divider() 
        print('El CÓDIGO debe ser numérico, entre 4 y 6 cifras.')
        self.show_divider() 

    def show_invalid_name(self):
        # Muestra un mensaje de requisitos de nombre.
        self.show_divider()
        print('El NOMBRE debe tener menos 3 letras.')
        self.show_divider()

    def show_invalid_price(self):
        # Muestra un mensaje de requisitos del precio.
        self.show_divider()
        print('El PRECIO debe ser numérico mayor que 0.')
        self.show_divider()

    def show_invalid_stock(self):
        # Muestra un mensaje de requisitos del stock.
        self.show_divider()
        print('El STOCK debe ser numérico mayor o igual a 0.') 
        self.show_divider()

    def show_closing_program(self):
        # Muestra un mensaje de cierre del programa.
        self.show_divider()
        print(f'GRACIAS por usar {Back.YELLOW}{Fore.BLACK}E-commerce Console{Back.RESET}{Fore.RESET}.\nSaliendo del programa...')
        self.show_divider()

    def paginate_list(self, items, page_size):
        # Divide una lista en páginas de tamaño fijo.
        return [items[i:i + page_size] for i in range(0, len(items), page_size)]    

    def show_paginated_controls(self, current_page, total_pages):
        # Muestra controles de paginación.
        self.show_divider()
        print(f'Página {current_page + 1} de {total_pages}. Opciones: [{Fore.YELLOW}S{Fore.RESET}] Siguiente | [{Fore.YELLOW}A{Fore.RESET}] Anterior | [{Fore.YELLOW}V{Fore.RESET}] Volver')
        self.show_divider()
    
    def show_main_menu(self): 
        self.show_divider()       
        print(f'Menú {Back.YELLOW}{Fore.BLACK} E-commerce Console {Back.RESET}{Fore.RESET}, Escriba número de opción ({Fore.YELLOW}1-7{Fore.RESET}):'.center(50))
        self.show_divider()
        self.show_divider()
        print(f'\t [{Fore.YELLOW}1{Fore.RESET}] {Fore.GREEN}Agregar Producto')
        print(f'\t [{Fore.YELLOW}2{Fore.RESET}] {Fore.WHITE}Listar Productos')
        print(f'\t [{Fore.YELLOW}3{Fore.RESET}] {Fore.BLUE}Buscar Producto')
        print(f'\t [{Fore.YELLOW}4{Fore.RESET}] {Fore.MAGENTA}Actualizar Producto')
        print(f'\t [{Fore.YELLOW}5{Fore.RESET}] {Fore.CYAN}Reportes de Productos')
        print(f'\t [{Fore.YELLOW}6{Fore.RESET}] {Fore.RED}Eliminar Producto')
        print(f'\t [{Fore.YELLOW}7{Fore.RESET}] Salir')
        self.show_divider()

    def show_dynamic_menu(self, title):
        title = title.upper()
        self.show_title_menu_dynamic(f'{title} Producto', '1-4')
        self.show_divider()
        print(f'\t [{Fore.YELLOW}1{Fore.RESET}] {Fore.GREEN}{title} Producto por ID')
        print(f'\t [{Fore.YELLOW}2{Fore.RESET}] {Fore.WHITE}{title} Producto por CÓDIGO')
        print(f'\t [{Fore.YELLOW}3{Fore.RESET}] {Fore.BLUE}{title} Producto por NOMBRE')
        print(f'\t [{Fore.YELLOW}4{Fore.RESET}] Volver')
        self.show_divider()
    
    def show_report_menu(self):        
        self.show_title_menu_dynamic('REPORTES de Productos', '1-3')
        self.show_divider()
        print(f'\t [{Fore.YELLOW}1{Fore.RESET}] {Fore.YELLOW}Productos Bajo de Stock')
        print(f'\t [{Fore.YELLOW}2{Fore.RESET}] {Fore.RED}Productos ELIMINADOS')
        print(f'\t [{Fore.YELLOW}3{Fore.RESET}] Volver')
        self.show_divider()

    def show_input(self, text):
        self.show_divider()
        prompt = input(f'{text}').strip()
        return prompt