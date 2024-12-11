class ProductView:
    @staticmethod
    def display_products(products):
        if not products:
            print("No hay productos registrados.")
        else:
            for product in products:
                print(f"ID: {product[0]}, Código: {product[1]}, Nombre: {product[2]}, Precio: {product[3]}, Stock: {product[4]}")

    @staticmethod
    def display_message(message):
        print(message)

    @staticmethod
    def get_input(prompt):
        return input(prompt)
