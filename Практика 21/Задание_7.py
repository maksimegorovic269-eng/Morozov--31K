# Задание 7
# Класс Point со слотами и методом вывода координат

class Point:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def coordinates(self):
        return f"Координаты точки: x = {self.x}, y = {self.y}"


point = Point(10, 20)
print(point.coordinates())
