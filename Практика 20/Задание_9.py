# Задание 9 – Счётчик обращений

class CounterDescriptor:
    def __init__(self):
        self.count = 0

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        self.count += 1
        print(f"Количество обращений: {self.count}")
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class Test:
    attr = CounterDescriptor()


obj = Test()
obj.attr = 50

print(obj.attr)
print(obj.attr)
print(obj.attr)
