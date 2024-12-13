from src.views.addons_view import AddonsView

addons_view = AddonsView()

def validate_back(prompt):
    return prompt.lower() != 'v'

def validate_id(id):
    return validate_back(id) and id.isnumeric() and int(id) > 0

def validate_code(code):
    return validate_back(code) and len(code) >= 4 and code.isnumeric() and int(code) >= 1000 and int(code) <= 999999

def validate_name(name):
    return validate_back(name) and len(name) >= 3 and name.isalpha() and len(name) < 255

def validate_price(price):
    return validate_back(price) and  price.replace('.', '', 1).isdigit() and float(price) > 0 and float(price) < 9223372036854775807

def validate_stock(stock):
    return validate_back(stock) and stock.isnumeric() and int(stock) >= 0

def validated_input(prompt, current_value, validation_func=None, allow_skip=True):
    input_valid = False  # Variable de control para el bucle
    while not input_valid:
        try:
            user_input = addons_view.show_input(prompt).title() if 'nombre' in prompt.lower() else addons_view.show_input(prompt)

            if user_input.lower() == 'v':                
                return 'v'

            if user_input == '' and allow_skip: # Para cuando quieren actualizar y dejar el valor previo
                return current_value

            if validation_func and not validation_func(user_input):                               
                addons_view.show_invalid_data()
            else:
                input_valid = True  # Cambiar la bandera a True si la entrada es válida
                return user_input

        except ValueError as ve:
            print(f'Error en la entrada: {ve}. Inténtalo de nuevo.')
        except Exception as e:
            print(f'Ocurrió un error inesperado: {e}. Inténtalo de nuevo.')