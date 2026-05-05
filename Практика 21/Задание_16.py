# Задание 16
# Класс Temperature со слотами и переводом из Цельсия в Фаренгейт

class Temperature:
    __slots__ = ("value",)

    def __init__(self, value):
        self.value = value

    def to_fahrenheit(self):
        return self.value * 9 / 5 + 32


temperature = Temperature(25)

print("Температура в Цельсиях:", temperature.value)
print("Температура в Фаренгейтах:", temperature.to_fahrenheit())
