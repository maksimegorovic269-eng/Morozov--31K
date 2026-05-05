# Задание 11
# Класс Product со слотами и проверкой цены

class Product:
    __slots__ = ("name", "price")

    def __init__(self, name, price):
        self.name = name
        self.set_price(price)

    def set_price(self, price):
        if price < 0:
            raise ValueError("Цена не может быть отрицательной")
        self.price = price


product = Product("Ноутбук", 70000)

print("Товар:", product.name)
print("Цена:", product.price)

try:
    product.set_price(-100)
except ValueError as error:
    print("Ошибка:", error)
