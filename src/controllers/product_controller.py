from src.models.product_model import ProductModel
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
addons_view = AddonsView()
product_view = ProductView()
class ProductController:    

    def create_product(self):
        while True:
            addons_view.display_title_menu('Agregar Producto', 'V', 'letra')
            addons_view.display_back_menu()
            product_view.display_product_requirements()
            code = validated_input('\tIngrese el código numérico del producto (mín. 4 dígitos): ', '', validate_code, allow_skip=False)
            if code.lower() == 'v':
                addons_view.clear_screen() 
                break
            addons_view.display_divider()
            name = validated_input('\tIngrese el nombre del producto: ', '', validate_name, allow_skip=False)
            if name.lower() == 'v': 
                addons_view.clear_screen()
                break
            addons_view.display_divider()
            price = validated_input('\tIngrese el precio del producto: ', '', validate_price, allow_skip=False)
            if price.lower() == 'v':
                addons_view.clear_screen()
                break
            addons_view.display_divider()
            stock = validated_input('\tIngrese el stock inicial: ', '', validate_stock, allow_skip=False)
            if stock.lower() == 'v':
                addons_view.clear_screen()
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
        addons_view.display_title_menu(f'Buscador por {condition}', 'V', 'letra')
        addons_view.display_back_menu()
        condition = condition.upper()
        product = {}
        back = False
        product_exist = False
        while not back:
            prompt = input(f'\t Ingrese el {condition} del producto a BUSCAR: ').strip()           
            if not validate_back(prompt) and (back := True):
                addons_view.clear_screen()
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
                
            addons_view.clear_screen()
            addons_view.display_title_menu(f'Buscador por {condition}', 'V', 'letra')
            addons_view.display_back_menu()
            if product_exist:
                product_view.display_table_headers()
                product_view.display_product(product)
                addons_view.display_divider()
            else:
                addons_view.display_not_found(f'producto con {condition} : {prompt}')   

    def update_product(self):
        try:
            product_id = int(self.addons_view.get_input("Ingrese el ID del producto a actualizar: "))
            code = int(self.addons_view.get_input("Ingrese el nuevo código del producto: "))
            name = self.addons_view.get_input("Ingrese el nuevo nombre del producto: ")
            price = float(self.addons_view.get_input("Ingrese el nuevo precio del producto: "))
            stock = int(self.addons_view.get_input("Ingrese el nuevo stock del producto: "))
            self.product_model.update_product(product_id, code, name, price, stock)
            self.addons_view.display_message("Producto actualizado exitosamente.")
        except ValueError:
            self.addons_view.display_message("Error: Entrada inválida. Intente nuevamente.")

    def delete_product(self):
        try:
            product_id = int(self.addons_view.get_input("Ingrese el ID del producto a eliminar: "))
            self.product_model.delete_product(product_id)
            self.addons_view.display_message("Producto eliminado exitosamente.")
        except ValueError:
            self.addons_view.display_message("Error: Entrada inválida. Intente nuevamente.")
