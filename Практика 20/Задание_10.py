# Задание 10 – Ограничение длины

class LengthDescriptor:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError("Значение должно быть строкой")
        if len(value) > 10:
            raise ValueError("Длина строки должна быть не более 10 символов")
        instance.__dict__[self.name] = value


class Test:
    text = LengthDescriptor()


obj = Test()
obj.text = "Python"
print(obj.text)
