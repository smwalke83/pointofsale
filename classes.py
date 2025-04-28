class Product:
    def __init__(self, name, description, price, quantity, UPC):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        self.UPC = UPC
        self.is_flagged = False

class Catalogue:
    def __init__(self):
        self.dict = {}
