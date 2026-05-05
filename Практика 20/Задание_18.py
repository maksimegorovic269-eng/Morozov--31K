# Задание 18 – Список чисел

class NumberListDescriptor:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not isinstance(value, list):
            raise TypeError("Значение должно быть списком")

        for item in value:
            if not isinstance(item, (int, float)):
                raise TypeError("Все элементы списка должны быть числами")

        instance.__dict__[self.name] = value


class Test:
    numbers = NumberListDescriptor()


obj = Test()
obj.numbers = [1, 2, 3, 4.5]
print(obj.numbers)
