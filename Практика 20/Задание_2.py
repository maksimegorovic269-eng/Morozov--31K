# Задание 2 – Дескриптор с логированием

class LoggingDescriptor:
    def __init__(self):
        self.value = None

    def __get__(self, instance, owner):
        print("Getting value")
        return self.value

    def __set__(self, instance, value):
        self.value = value


class Test:
    attr = LoggingDescriptor()


obj = Test()
obj.attr = 25
print(obj.attr)
