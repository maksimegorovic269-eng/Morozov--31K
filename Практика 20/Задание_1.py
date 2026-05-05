# Задание 1 – Простой дескриптор

class SimpleDescriptor:
    def __init__(self):
        self.value = None

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = value


class Test:
    attr = SimpleDescriptor()


obj = Test()
obj.attr = 10
print(obj.attr)
