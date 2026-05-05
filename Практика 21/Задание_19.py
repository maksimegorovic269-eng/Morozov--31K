# Задание 19
# Класс Order со слотами и подсчётом общей стоимости

class Order:
    __slots__ = ("items",)

    def __init__(self, items):
        self.items = items

    def total_price(self):
        return sum(self.items)


order = Order([100, 250, 300, 150])

print("Цены товаров:", order.items)
print("Общая стоимость заказа:", order.total_price())
