# Задание 4 – Приватное хранение

class PrivateDescriptor:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class Test:
    attr = PrivateDescriptor()


obj = Test()
obj.attr = "Python"
print(obj.attr)
print(obj.__dict__)
