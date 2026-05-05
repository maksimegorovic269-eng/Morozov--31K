# Задание 7 – Строковый дескриптор

class StringDescriptor:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError("Можно устанавливать только строки")
        instance.__dict__[self.name] = value


class Test:
    text = StringDescriptor()


obj = Test()
obj.text = "Hello"
print(obj.text)
