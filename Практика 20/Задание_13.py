# Задание 13 – Округление

class RoundDescriptor:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = round(value, 2)


class Test:
    number = RoundDescriptor()


obj = Test()
obj.number = 15.6789
print(obj.number)
