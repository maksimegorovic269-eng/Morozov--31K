# Задание 6 – Положительные числа

class PositiveDescriptor:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError("Число должно быть положительным")
        instance.__dict__[self.name] = value


class Test:
    number = PositiveDescriptor()


obj = Test()
obj.number = 7
print(obj.number)
