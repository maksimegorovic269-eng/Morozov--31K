# Задание 14
# Класс Vector со слотами и методом сложения векторов

class Vector:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def show(self):
        return f"Vector({self.x}, {self.y})"


v1 = Vector(2, 3)
v2 = Vector(4, 5)

result = v1.add(v2)

print("Первый вектор:", v1.show())
print("Второй вектор:", v2.show())
print("Сумма векторов:", result.show())
