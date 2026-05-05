# Задание 5 – Ограничение типа

class IntDescriptor:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError("Можно устанавливать только int")
        instance.__dict__[self.name] = value


class Test:
    number = IntDescriptor()


obj = Test()
obj.number = 15
print(obj.number)
