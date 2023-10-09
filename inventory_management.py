class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Product ID: {self.product_id}\nName: {self.name}\nPrice: ${self.price:.2f}\nQuantity: {self.quantity}\n"

class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        if product.product_id not in self.products:
            self.products[product.product_id] = product
            print(f"Product '{product.name}' added to inventory.")
        else:
            print(f"Product with ID {product.product_id} already exists in inventory.")

    def remove_product(self, product_id):
        if product_id in self.products:
            removed_product = self.products.pop(product_id)
            print(f"Product '{removed_product.name}' removed from inventory.")
        else:
            print(f"Product with ID {product_id} not found in inventory.")

    def list_products(self):
        if not self.products:
            print("Inventory is empty.")
        else:
            for product_id, product in self.products.items():
