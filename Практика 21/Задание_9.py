# Задание 9
# Класс Circle со слотами и методом вычисления площади круга

import math


class Circle:
    __slots__ = ("radius",)

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


circle = Circle(3)
print("Площадь круга:", round(circle.area(), 2))
