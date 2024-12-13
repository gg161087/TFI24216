import time
from src.models.product_model import ProductModel
from src.models.product_removed_model import ProductRemovedModel
from src.views.addons_view import AddonsView
from src.views.product_view import ProductView
from src.utils.validator_input import (
    validate_back,
    validate_id,
    validate_code,
    validate_name,
    validate_price,
    validate_stock,
    validated_input
)

product_model = ProductModel()
product_removed_model = ProductRemovedModel()
addons_view = AddonsView()
product_view = ProductView()
class ProductController:    

    def create_product(self):
        confirm = False
        back = False
        addons_view.clear_screen()
        addons_view.show_title_menu('Agregar Producto')
        product_view.show_product_requirements()
        while not back:
            code = validated_input('\tIngrese el código (debe ser numérico, entre 4 y 6 cifras): ', '', validate_code, allow_skip=False)
            if code.lower() == 'v':
                addons_view.clear_screen()                        
                addons_view.show_main_menu() 
                break
            addons_view.show_divider()
            name = validated_input('\tIngrese el nombre (debe tener menos 3 letras): ', '', validate_name, allow_skip=False)
            if name.lower() == 'v': 
                addons_view.clear_screen()
                addons_view.show_main_menu()
                break
            addons_view.show_divider()
            price = validated_input('\tIngrese el precio (debe ser numérico y mayor que 0): ', '', validate_price, allow_skip=False)
            if price.lower() == 'v':
                addons_view.clear_screen()
                addons_view.show_main_menu()
                break
            addons_view.show_divider()
            stock = validated_input('\tIngrese el stock (debe ser numérico y mayor o igual a 0): ', '', validate_stock, allow_skip=False)
            if stock.lower() == 'v':
                addons_view.clear_screen()
                addons_view.show_main_menu()
                break
            addons_view.show_divider()
            if code and name and price and stock:
                if product_model.create_product(int(code), name, float(price), int(stock)):
                    addons_view.clear_screen()
                    addons_view.show_title_menu('Agregar Producto')                    
                    addons_view.show_message(f'Producto "{name}" agregado con éxito.')
                    product = product_model.read_product_dynamic('name', name)
                    if product:
                        product_view.show_table_headers()
                        product_view.show_product(product)
                        addons_view.show_confirm('AGREGAR OTRO PRODUCTO')
                        while not confirm:
                            prompt_confirm = addons_view.show_input('\t Seleccione una opción: ').strip().lower()
                            if prompt_confirm.lower() == 's':
                                addons_view.clear_screen()
                                addons_view.show_title_menu('Agregar Producto')
                                product_view.show_product_requirements()
                                confirm = True
                            elif prompt_confirm.lower() == 'n':
                                addons_view.clear_screen()
                                addons_view.show_main_menu()
                                confirm = True
                                back = True
                            else:
                                addons_view.clear_screen()
                                addons_view.show_title_menu('Agregar Producto')
                                addons_view.show_invalid_option()
                                addons_view.show_confirm('AGREGAR OTRO PRODUCTO')

    def list_products(self):
        products = product_model.read_all_products()
        if products:
            product_view.show_products(products, 'Productos')
        else:
            addons_view.show_message('No se encontraron PRODUCTOS.')
    
    def search_product_dynamic(self, product, condition):
        addons_view.clear_screen()
        addons_view.show_title_menu(f'Buscador por {condition}')
        product_view.show_table_headers()
        product_view.show_product(product)
        addons_view.show_divider()

    def update_product_dynamic(self, product, condition):
        confirm = False
        addons_view.clear_screen()
        addons_view.show_title_menu(f'Actualizar el Producto {product['name']}')
        product_view.show_table_headers()
        product_view.show_product(product)
        addons_view.show_divider()
        product_view.show_product_requirements()
        new_code = validated_input('\tNuevo código(Presione enter para dejar el que estaba): ', product['code'], validate_code)
        if new_code == 'v':
            addons_view.clear_screen()
            addons_view.show_title_menu(f'ACTUALIZAR por {condition}') 
            return
        new_name = validated_input('\tNuevo nombre(Presione enter para dejar el que estaba): ', product['name'], validate_name)
        if new_name == 'v':
            addons_view.clear_screen()
            addons_view.show_title_menu(f'ACTUALIZAR por {condition}')
            return                    
        new_price = validated_input('\tNuevo precio(Presione enter para dejar el que estaba): ', product['price'], validate_price)
        if new_price == 'v':
            addons_view.clear_screen()
            addons_view.show_title_menu(f'ACTUALIZAR por {condition}') 
            return
        new_stock = validated_input('\tNuevo stock(Presione enter para dejar el que estaba): ', product['stock'], validate_stock)
        if new_stock == 'v':
            addons_view.clear_screen()
            addons_view.show_title_menu(f'ACTUALIZAR por {condition}')
            return                    
        new_product = {
            'id': product['id'],
            'code': int(new_code),
            'name': new_name,
            'price': float(new_price),
            'stock': int(new_stock)
        }
        addons_view.clear_screen()
        addons_view.show_title_menu_dynamic(f'Actualizar el Producto {product['name']}', 'S-N', 'letra')
        product_view.show_table_headers()
        product_view.show_product(new_product)
        addons_view.show_divider()
        addons_view.show_confirm('ACTUALIZAR')
        while not confirm:
            prompt_confirm = addons_view.show_input('\t Seleccione una opción: ').strip().lower()
            if prompt_confirm == 's':
                if product_model.update_product(int(product['id']), int(new_code), new_name, float(new_price), int(new_stock)):
                    addons_view.clear_screen()
                    addons_view.show_title_menu(f'ACTUALIZAR por {condition}')
                    addons_view.show_message(f'Producto {product['name']} actualizado correctamente.')                                      
                    break
            elif prompt_confirm == 'n':
                addons_view.clear_screen()
                addons_view.show_title_menu(f'ACTUALIZAR por {condition}')
                break                            
            else:
                addons_view.show_invalid_option()

    def delete_product_dynamic(self, product, condition):
        confirm = False
        addons_view.clear_screen()
        addons_view.show_title_menu_dynamic(f'Eliminar {product['name']}', 'S-N', 'letra')        
        product_view.show_table_headers()
        product_view.show_product(product)
        addons_view.show_confirm('ELIMINAR')
        while not confirm:
            prompt_confirm = addons_view.show_input('\t Seleccione una opción: ').strip().lower()
            if prompt_confirm.lower() == 's':
                if product_model.delete_product(int(product['id'])):
                    addons_view.clear_screen()
                    product_removed_model.create_product_removed(product['code'], product['name'], product['price'], product['stock'])
                    addons_view.show_title_menu(f'ELIMINAR por {condition}')
                    addons_view.show_message(f'Producto {product['name']} eliminado correctamente.')
                    break
            elif prompt_confirm.lower() == 'n':
                addons_view.clear_screen()                
                addons_view.show_title_menu(f'ELIMINAR por {condition}')
                break                            
            else:
                addons_view.clear_screen()
                addons_view.show_title_menu_dynamic(f'Eliminar {product['name']}', 'S-N', 'letra')
                product_view.show_table_headers()
                product_view.show_product(product)
                addons_view.show_divider()
                addons_view.show_confirm('ELIMINAR')
                addons_view.show_invalid_option()
    
    def dynamic_product_controller(self, title, condition):
        title = title.upper()
        condition = condition.upper()
        addons_view.show_title_menu(f'{title} por {condition}')
        back = False
        while not back:
            invalid = False
            not_found = False
            prompt = addons_view.show_input(f'\t Ingrese el {condition} del producto a {title}: ').strip()           
            if not validate_back(prompt) and (back := True):
                addons_view.clear_screen()
                addons_view.show_dynamic_menu(f'{title}')
                break
            else:
                if condition == 'ID':
                    if validate_id(prompt):
                        id = int(prompt)
                        product = product_model.read_product_dynamic('id', id)
                        if product:
                            if title == 'ELIMINAR':
                                self.delete_product_dynamic(product, condition)
                            elif title == 'ACTUALIZAR':
                                self.update_product_dynamic(product, condition)
                            else:
                                self.search_product_dynamic(product, condition)
                        else:
                            not_found = True
                    else:
                        invalid = True
                elif condition == 'CÓDIGO':
                    if validate_code(prompt):
                        code = int(prompt)
                        product = product_model.read_product_dynamic('code', code)
                        if product:
                            if title == 'ELIMINAR':
                                self.delete_product_dynamic(product, condition)
                            elif title == 'ACTUALIZAR':
                                self.update_product_dynamic(product, condition)
                            else:
                                self.search_product_dynamic(product, condition)
                        else:
                            not_found = True                            
                    else:
                        invalid = True
                else:
                    if validate_name(prompt):
                        name = prompt.title()
                        product = product_model.read_product_dynamic('name', name)
                        if product:
                            if title == 'ELIMINAR':
                                self.delete_product_dynamic(product, condition)
                            elif title == 'ACTUALIZAR':
                                self.update_product_dynamic(product, condition)
                            else:
                                self.search_product_dynamic(product, condition)
                        else:
                            not_found = True
                    else:
                        invalid = True
                if invalid:
                    addons_view.clear_screen()
                    addons_view.show_title_menu(f'{title} por {condition}')
                    match condition:
                        case 'ID':
                            addons_view.show_invalid_id()
                        case 'CÓDIGO':
                            addons_view.show_invalid_code()
                        case 'NOMBRE':
                            addons_view.show_invalid_name()
                        case _:
                            addons_view.show_message(f'PRODCUTO con {condition}: {prompt}, no encontrado')
                if not_found:
                    addons_view.clear_screen()
                    addons_view.show_title_menu(f'{title} por {condition}')
                    addons_view.show_message(f'PRODCUTO con {condition}: {prompt}, no encontrado')

    def low_stock_report_controller(self):
        products = product_model.read_low_stock_products()
        if products:        
            product_view.show_products(products, 'REPORTE de PRODUCTOS con STOCK BAJO', report=True)
        else:
            addons_view.show_message('No se encontraron PRODUCTOS con STOCK BAJO')
            time.sleep(3)
