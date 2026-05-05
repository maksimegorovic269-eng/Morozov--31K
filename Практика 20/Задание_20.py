# Задание 20 – Комплексный дескриптор

class ComplexDescriptor:
    def __init__(self, data_type, min_value=None, max_value=None):
        self.data_type = data_type
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        print("Получение значения")
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        print("Установка значения")

        if not isinstance(value, self.data_type):
            raise TypeError(f"Значение должно быть типа {self.data_type.__name__}")

        if self.min_value is not None and value < self.min_value:
            raise ValueError("Значение меньше допустимого")

        if self.max_value is not None and value > self.max_value:
            raise ValueError("Значение больше допустимого")

        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        raise AttributeError("Удаление запрещено")


class Test:
    age = ComplexDescriptor(int, 0, 120)


obj = Test()
obj.age = 25
print(obj.age)

# del obj.age  # Будет ошибка
