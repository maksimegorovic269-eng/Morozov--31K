# Задание 8 – Значение по умолчанию

class DefaultDescriptor:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name, "default")

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class Test:
    attr = DefaultDescriptor()


obj = Test()
print(obj.attr)

obj.attr = "Новое значение"
print(obj.attr)
