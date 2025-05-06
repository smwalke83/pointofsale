from enum import Enum

class Product:
    def __init__(self, name, description, price, quantity, UPC):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        self.UPC = UPC
        self.is_low = False
        self.is_out = False
    
    def __repr__(self):
        return f"Product Name: {self.name}, Description: {self.description}, Price: ${self.price}, Quantity: {self.quantity}, UPC: {self.UPC}"

class Catalogue:
    def __init__(self):
        self.dict = {}
        self.sales = 0.0


