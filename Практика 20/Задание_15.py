# Задание 15 – Лог изменений

class ChangeLogDescriptor:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        old_value = instance.__dict__.get(self.name, None)
        print(f"Старое значение: {old_value}")
        print(f"Новое значение: {value}")
        instance.__dict__[self.name] = value


class Test:
    attr = ChangeLogDescriptor()


obj = Test()
obj.attr = 10
obj.attr = 20
print(obj.attr)
