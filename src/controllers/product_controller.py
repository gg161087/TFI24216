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
        addons_view.clear_screen()
        addons_view.display_title_menu('Agregar Producto')
        product_view.display_product_requirements()
        while True:
            code = validated_input('\tIngrese el código numérico del producto (mín. 4 dígitos): ', '', validate_code, allow_skip=False)
            if code.lower() == 'v':
                addons_view.clear_screen()                        
                addons_view.display_menu() 
                break
            addons_view.display_divider()
            name = validated_input('\tIngrese el nombre del producto: ', '', validate_name, allow_skip=False)
            if name.lower() == 'v': 
                addons_view.clear_screen()
                addons_view.display_menu()
                break
            addons_view.display_divider()
            price = validated_input('\tIngrese el precio del producto: ', '', validate_price, allow_skip=False)
            if price.lower() == 'v':
                addons_view.clear_screen()
                addons_view.display_menu()
                break
            addons_view.display_divider()
            stock = validated_input('\tIngrese el stock inicial: ', '', validate_stock, allow_skip=False)
            if stock.lower() == 'v':
                addons_view.clear_screen()
                addons_view.display_menu()
                break
            addons_view.display_divider()
            if code and name and price and stock:
                if product_model.create_product(int(code), name, float(price), int(stock)):
                    addons_view.clear_screen()
                    addons_view.display_divider()
                    addons_view.display_message(f'Producto "{name}" agregado con éxito.')                    
                    addons_view.display_divider()
                    product = product_model.read_product_dynamic('name', name)
                    if product:
                        product_view.display_table_headers()
                        product_view.display_product(product)
                        break

    def list_products(self):
        products = product_model.read_all_products()
        if products:
            product_view.display_products(products, 'Productos')
        else:
            addons_view.display_not_found()

    def search_product_dynamic(sef, condition):
        addons_view.display_title_menu(f'Buscador por {condition}')
        product = {}
        back = False
        product_exist = False
        while not back:
            prompt = input(f'\t Ingrese el {condition} del producto a BUSCAR: ').strip()           
            if not validate_back(prompt) and (back := True):
                addons_view.clear_screen()
                addons_view.display_dynamic_selector('BUSCAR')
                break
            else:                
                if condition == 'ID':
                    if validate_id(prompt):
                        product_id = int(prompt)
                        product = product_model.read_product_dynamic('id', product_id)
                        if product:
                            product_exist = True
                    else:
                        addons_view.display_invalid_id()
                elif condition == 'CÓDIGO':
                    if validate_code(prompt):
                        code = int(prompt)
                        product = product_model.read_product_dynamic('code', code)
                        if product:
                            product_exist = True
                    else:
                        addons_view.display_invalid_code() 
                else:
                    if validate_name(prompt):
                        name = prompt.capitalize()
                        product = product_model.read_product_dynamic('name', name)
                        if product:
                            product_exist = True
                    else:
                        addons_view.display_invalid_name()                
            if product_exist:
                addons_view.clear_screen()
                addons_view.display_title_menu(f'Buscador por {condition}')
                product_view.display_table_headers()
                product_view.display_product(product)
                addons_view.display_divider()
            else:
                addons_view.clear_screen()
                addons_view.display_title_menu(f'Buscador por {condition}')
                addons_view.display_not_found(f'producto con {condition}: {prompt}')

    def update_product_controller(self, product, condition):
        confirm = False
        addons_view.clear_screen()
        addons_view.display_title_menu(f'Actualizar el Producto {product['name']}')
        product_view.display_table_headers()
        product_view.display_product(product)
        addons_view.display_divider()
        product_view.display_product_requirements()
        new_code = validated_input('\tNuevo código(Presione enter para dejar el que estaba): ', product['code'], validate_code)
        if new_code == 'v':
            addons_view.clear_screen()
            addons_view.display_title_menu(f'Buscador por {condition}') 
            return
        new_name = validated_input('\tNuevo nombre(Presione enter para dejar el que estaba): ', product['name'], validate_name)
        if new_name == 'v':
            addons_view.clear_screen()
            addons_view.display_title_menu(f'Buscador por {condition}')
            return                    
        new_price = validated_input('\tNuevo precio(Presione enter para dejar el que estaba): ', product['price'], validate_price)
        if new_price == 'v':
            addons_view.clear_screen()
            addons_view.display_title_menu(f'BUSCAR y ACTUALIZAR') 
            return
        new_stock = validated_input('\tNuevo stock(Presione enter para dejar el que estaba): ', product['stock'], validate_stock)
        if new_stock == 'v':
            addons_view.clear_screen()
            addons_view.display_title_menu(f'Buscador por {condition}')
            return                    
        new_product = {
            'id': product['id'],
            'code': int(new_code),
            'name': new_name,
            'price': float(new_price),
            'stock': int(new_stock)
        }
        addons_view.clear_screen()
        addons_view.display_divider()
        product_view.display_table_headers()
        product_view.display_product(new_product)
        addons_view.display_divider()
        addons_view.display_confirm('ACTUALIZAR')
        while not confirm:
            prompt_confirm = input('\t Seleccione una opción: ').strip().lower()
            if prompt_confirm == 's':
                if self.update_product(int(product['id']), int(new_code), new_name, float(new_price), int(new_stock)):
                    print('Producto actualizado correctamente.')
                    time.sleep(3)
                    break
            elif prompt_confirm == 'n':
                addons_view.clear_screen()
                addons_view.display_back_menu()
                break                            
            else:
                addons_view.display_invalid_option()

    def update_product_dynamic(self, condition):
        addons_view.display_title_menu(f'Buscador por {condition}')
        back = False
        while not back:
            prompt = input(f'\t Ingrese el {condition} del producto a BUSCAR: ').strip()           
            if not validate_back(prompt) and (back := True):
                addons_view.clear_screen()
                addons_view.display_dynamic_selector('ACTUALIZAR')
                break
            else:
                if condition == 'ID':
                    if validate_id(prompt):
                        id = int(prompt)
                        product = product_model.read_product_dynamic('id', id)
                        if product:
                            self.update_product_controller(product, condition)          
                        else:
                            addons_view.display_not_found(f'producto con ID: {id}')                        
                    else:
                        addons_view.display_invalid_id()
                elif condition == 'CÓDIGO':
                    if validate_code(prompt):
                        code = int(prompt)
                        product = product_model.read_product_dynamic('code', code)
                        if product:
                            self.update_product_controller(product, condition)         
                        else:
                            addons_view.display_not_found(f'producto con CODIGO: {code}')
                    else:
                        addons_view.display_invalid_code()                        
                else:
                    if validate_name(prompt): 
                        name = prompt.capitalize()                   
                        product = product_model.read_product_dynamic('id', id)
                        if product:
                            self.update_product_controller(product, condition)          
                        else:
                            addons_view.display_not_found(f'producto con NOMBRE: {name}') 
                    else:
                        addons_view.display_invalid_name() 

    def delete_product_dynamic(self, condition):
        addons_view.display_title_menu(f'Eliminar por {condition}')
        back = False
        confirm = False
        while not back:
            prompt = input(f'\t Ingrese el {condition} del producto a ELIMINAR: ').strip()           
            if not validate_back(prompt) and (back := True):
                addons_view.clear_screen()
                addons_view.display_dynamic_selector('Eliminar')
                break
            else:
                if condition == 'ID':
                    if validate_id(prompt):
                        id = int(prompt)
                        product = product_model.read_product_dynamic('id', id)
                        if product:
                            addons_view.clear_screen()
                            addons_view.display_title_menu_dynamic(f'Eliminar {product['name']}', 'S-N', 'letra')        
                            product_view.display_table_headers()
                            product_view.display_product(product)
                            addons_view.display_confirm('ELIMINAR')
                            while not confirm:
                                prompt_confirm = input('\t Seleccione una opción: ').strip().lower()
                                if prompt_confirm == 's':
                                    if product_model.delete_product(int(product['id'])):
                                        product_removed_model.create_product_removed(product['code'], product['name'], product['price'], product['stock'])
                                        addons_view.display_remove_message()
                                        break
                                elif prompt_confirm == 'n':
                                    addons_view.clear_screen()
                                    addons_view.display_title_menu(f'ELIMINAR por {condition}')
                                    break                            
                                else:
                                    addons_view.clear_screen()
                                    addons_view.display_title_menu_dynamic(f'Eliminar {product['name']}', 'S-N', 'letra')
                                    product_view.display_table_headers()
                                    product_view.display_product(product)
                                    addons_view.display_divider()
                                    addons_view.display_confirm('ELIMINAR')
                                    addons_view.display_invalid_option()                                                                  
                        else:
                            addons_view.clear_screen()
                            addons_view.display_title_menu(f'ELIMINAR por {condition}')                           
                            addons_view.display_not_found(f'producto con ID: {id}')                 
                    else:
                        addons_view.clear_screen()
                        addons_view.display_title_menu(f'ELIMINAR por {condition}')
                        addons_view.display_invalid_id() 
                elif condition == 'CÓDIGO':
                    if validate_code(prompt):
                        code = int(prompt)
                        product = product_model.read_product_dynamic('code', code)
                        if product:
                            addons_view.clear_screen()
                            addons_view.display_title_menu_dynamic(f'Eliminar {product['name']}', 'S-N', 'letra')
                            product_view.display_table_headers()
                            product_view.display_product(product)
                            addons_view.display_divider()
                            addons_view.display_confirm('ELIMINAR')
                            while not confirm:
                                prompt_confirm = input('\t Seleccione una opción: ').strip().lower()
                                if prompt_confirm == 's':
                                    if product_model.delete_product(int(product['id'])):
                                        product_removed_model.create_product_removed(product['code'], product['name'], product['price'], product['stock'])
                                        addons_view.clear_screen()
                                        addons_view.display_title_menu(f'Eliminar por {condition}')
                                        addons_view.display_message('Producto eliminado correctamente.')                                        
                                        break
                                elif prompt_confirm == 'n':
                                    addons_view.clear_screen()
                                    addons_view.display_title_menu(f'Eliminar por {condition}')
                                    break                            
                                else:
                                    addons_view.clear_screen()
                                    addons_view.display_title_menu_dynamic(f'Eliminar {product['name']}', 'S-N', 'letra')
                                    product_view.display_table_headers()
                                    product_view.display_product(product)
                                    addons_view.display_divider()
                                    addons_view.display_confirm(f'ELIMINAR por {condition}')
                                    addons_view.display_invalid_option()                                                    
                        else:
                            addons_view.clear_screen()
                            addons_view.display_title_menu(f'ELIMINAR por {condition}') 
                            addons_view.display_not_found(f'producto con CÓDIGO: {code}')
                    else:
                        addons_view.clear_screen()
                        addons_view.display_title_menu(f'ELIMINAR por {condition}')                        
                        addons_view.display_invalid_code()
                else:
                    if validate_name(prompt):
                        name = prompt.capitalize()
                        product = product_model.read_product_dynamic('name', name)
                        if product:
                            addons_view.clear_screen()
                            addons_view.display_divider()
                            product_view.display_table_headers()
                            product_view.display_product(product)
                            addons_view.display_divider()
                            addons_view.display_confirm('ELIMINAR')
                            while not confirm:
                                prompt_confirm = input('\t Seleccione una opción: ').strip().lower()
                                if prompt_confirm == 's':
                                    if product_model.delete_product(int(product['id'])):
                                        product_removed_model.create_product_removed(product['code'], product['name'], product['price'], product['stock'])
                                        addons_view.display_remove_message()
                                        break
                                elif prompt_confirm == 'n':
                                    addons_view.clear_screen()
                                    addons_view.display_title_menu(f'Eliminar por {condition}')
                                    break                            
                                else:
                                    addons_view.clear_screen()
                                    addons_view.display_title_menu_dynamic(f'Eliminar {product['name']}', 'S-N', 'letra')
                                    product_view.display_table_headers()
                                    product_view.display_product(product)
                                    addons_view.display_divider()
                                    addons_view.display_confirm(f'ELIMINAR por {condition}')
                                    addons_view.display_invalid_option()               
                        else:
                            addons_view.clear_screen()
                            addons_view.display_title_menu(f'ELIMINAR por {condition}') 
                            addons_view.display_not_found(f'producto con NOMBRE {name}')
                    else:
                        addons_view.clear_screen()
                        addons_view.display_title_menu(f'ELIMINAR por {condition}')                        
                        addons_view.display_invalid_name()
    
    def low_stock_report_controller(self):
        products = product_model.read_low_stock_products()
        if products:        
            product_view.display_products(products, 'REPORTE de PRODUCTOS con stock bajo')
        else:
            addons_view.display_not_found('productos con stock bajo')
            time.sleep(3)
