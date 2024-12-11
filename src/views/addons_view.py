import os
from colorama import Fore, Back, init

class AddonsView:
    def __init__(self):
        # Inicializa colorama con autoreset
        init(autoreset=True) 

    def clear_screen(self):
        # Limpia la consola según el sistema operativo.        
        os.system('cls' if os.name == 'nt' else 'clear') 

    def display_divider(self): 
        # Muestra un divisor decorativo.       
        print(Fore.YELLOW + '-' * 78) 

    def display_back_menu(self):
        # Muestra un mensaje para regresar al menú anterior.
        self.display_divider()
        print(f'Para volver al menú anterior escriba la letra [{Fore.YELLOW}V{Fore.RESET}]')
        self.display_divider()

    def display_title_menu(self, name, options, input_type='número'):
        # Muestra el título y las opciones de un menú.
        self.display_divider()
        print(f'Menú {name}, Escriba {input_type} de opción ({Fore.YELLOW}{options}{Fore.RESET}):'.center(50))
        self.display_divider()

    def display_confirm(self, action):
        # Muestra un mensaje de confirmación para una acción específica.
        self.display_divider()
        print(f'Desea {action}: [{Fore.YELLOW}S{Fore.RESET}] Si | [{Fore.YELLOW}N{Fore.RESET}] No')
        self.display_divider()
    
    def display_message(self, message):
        self.display_divider()
        print(message)
        self.display_divider()

    def display_invalid_data(self):
        self.display_divider()
        print('Datos ingresados incorrectos, intente de nuevo.')
        self.display_divider()

    def display_invalid_option(self, top_divider=True):
        # Muestra un mensaje de opción inválida.
        if top_divider:
            self.display_divider()
        print('\tOpción no válida, intente de nuevo.')
        self.display_divider()
    
    def display_invalid_id(self):
        # Muestra un mensaje de requisitos de id.    
        self.display_divider()
        print('El ID del producto debe ser numerico y mayor que 0.')
        self.display_divider()
    
    def display_invalid_code(self):
        # Muestra un mensaje de requisitos de code.
        self.display_divider() 
        print('El CÓDIGO debe ser numérico y de 4 cifras.')
        self.display_divider() 

    def display_invalid_name(self):
        # Muestra un mensaje de requisitos de nombre.
        self.display_divider()
        print('El NOMBRE del producto debe tener al menos 3 caracteres.')
        self.display_divider()

    def display_closing_program(self, program_name="E-commerce"):
        # Muestra un mensaje de cierre del programa.
        self.display_divider()
        print(f'GRACIAS por usar {Back.YELLOW}{Fore.BLACK}E-commerce Console{Back.RESET}{Fore.RESET}.\nSaliendo del programa...')
        self.display_divider()

    def paginate_list(self, items, page_size):
        # Divide una lista en páginas de tamaño fijo.
        return [items[i:i + page_size] for i in range(0, len(items), page_size)]    

    def display_paginated_controls(self, current_page, total_pages):
        # Muestra controles de paginación.
        self.display_divider()
        print(f'Página {current_page + 1} de {total_pages}. Opciones: [{Fore.YELLOW}S{Fore.RESET}] Siguiente | [{Fore.YELLOW}A{Fore.RESET}] Anterior | [{Fore.YELLOW}V{Fore.RESET}] Volver')
        self.display_divider()
    
    def display_menu(self):
        self.display_title_menu(f'{Back.YELLOW}{Fore.BLACK}E-commerce{Back.RESET}{Fore.RESET}', '1-7')
        self.display_divider()
        print(f'\t [{Fore.YELLOW}1{Fore.RESET}] {Fore.GREEN}Agregar Producto')
        print(f'\t [{Fore.YELLOW}2{Fore.RESET}] {Fore.WHITE}Listar Productos')
        print(f'\t [{Fore.YELLOW}3{Fore.RESET}] {Fore.BLUE}Buscar Producto')
        print(f'\t [{Fore.YELLOW}4{Fore.RESET}] {Fore.MAGENTA}Actualizar Producto')
        print(f'\t [{Fore.YELLOW}5{Fore.RESET}] {Fore.CYAN}Reportes de Productos')
        print(f'\t [{Fore.YELLOW}6{Fore.RESET}] {Fore.RED}Eliminar Producto')
        print(f'\t [{Fore.YELLOW}7{Fore.RESET}] Salir')
        self.display_divider()

    def display_dynamic_selector(self, selector):
        self.display_title_menu(f'{selector} Producto', '1-4')
        self.display_divider()
        print(f'\t [{Fore.YELLOW}1{Fore.RESET}] {Fore.GREEN}{selector} Producto por ID')
        print(f'\t [{Fore.YELLOW}2{Fore.RESET}] {Fore.WHITE}{selector} Producto por CÓDIGO')
        print(f'\t [{Fore.YELLOW}3{Fore.RESET}] {Fore.BLUE}{selector} Producto por NOMBRE')
        print(f'\t [{Fore.YELLOW}4{Fore.RESET}] Volver')
        self.display_divider()
    
    def display_report_menu(self):        
        self.display_title_menu('REPORTES de Productos', '1-3')
        self.display_divider()
        print(f'\t [{Fore.YELLOW}1{Fore.RESET}] {Fore.YELLOW}Productos Bajo de Stock')
        print(f'\t [{Fore.YELLOW}2{Fore.RESET}] {Fore.RED}Productos ELIMINADOS')
        print(f'\t [{Fore.YELLOW}3{Fore.RESET}] Volver')
        self.display_divider()
    
    def display_not_found(self, message):
        self.display_divider()
        print(f'No se encontró/encontraron {Fore.YELLOW}{message}{Fore.RESET}.'.center(50))
        self.display_divider()
    
    def display_remove_message(self):
        self.display_divider()
        print('Producto eliminado correctamente.')
        self.display_divider()