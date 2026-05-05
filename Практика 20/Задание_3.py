# Задание 3 – Дескриптор с установкой

class SetDescriptor:
    def __init__(self):
        self.value = None

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        print("Setting value")
        self.value = value


class Test:
    attr = SetDescriptor()


obj = Test()
obj.attr = 100
print(obj.attr)
