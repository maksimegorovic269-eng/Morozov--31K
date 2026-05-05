# Задание 17
# Класс Timer со слотами и вычислением разницы между временем

class Timer:
    __slots__ = ("start", "end")

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def difference(self):
        return self.end - self.start


timer = Timer(10, 25)

print("Начало:", timer.start)
print("Конец:", timer.end)
print("Разница:", timer.difference())
