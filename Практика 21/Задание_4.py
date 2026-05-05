# Задание 4
# Класс Car со слотами и конструктором

class Car:
    __slots__ = ("brand", "model", "year")

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year


car = Car("Toyota", "Camry", 2020)

print("Марка:", car.brand)
print("Модель:", car.model)
print("Год:", car.year)
