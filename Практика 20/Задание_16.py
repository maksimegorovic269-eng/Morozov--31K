# Задание 16 – Связанные поля

class PriceDescriptor:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value
        quantity = instance.__dict__.get("_quantity", 1)
        instance.__dict__["_total"] = value * quantity


class Product:
    price = PriceDescriptor()

    def __init__(self, quantity):
        self.__dict__["_quantity"] = quantity
        self.__dict__["_total"] = 0


product = Product(3)
product.price = 100

print(product.price)
print(product.__dict__["_total"])
