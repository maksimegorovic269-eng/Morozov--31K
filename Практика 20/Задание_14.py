# Задание 14 – Только одно присваивание

class OnceDescriptor:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if self.name in instance.__dict__:
            raise AttributeError("Изменение запрещено")
        instance.__dict__[self.name] = value


class Test:
    attr = OnceDescriptor()


obj = Test()
obj.attr = "Первое значение"
print(obj.attr)

# obj.attr = "Новое значение"  # Будет ошибка
