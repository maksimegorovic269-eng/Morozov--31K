# Задание 8
# Класс Rectangle со слотами и методом вычисления площади

class Rectangle:
    __slots__ = ("width", "height")

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


rectangle = Rectangle(5, 8)
print("Площадь прямоугольника:", rectangle.area())
