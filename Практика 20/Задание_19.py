# Задание 19 – Счётчик объектов

class ObjectCounter:
    count = 0

    def __init__(self):
        ObjectCounter.count += 1


obj1 = ObjectCounter()
obj2 = ObjectCounter()
obj3 = ObjectCounter()

print("Количество объектов:", ObjectCounter.count)
