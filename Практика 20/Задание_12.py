# Задание 12 – Возраст

class AgeDescriptor:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if value < 0 or value > 120:
            raise ValueError("Возраст должен быть от 0 до 120")
        instance.__dict__[self.name] = value


class Person:
    age = AgeDescriptor()


person = Person()
person.age = 20
print(person.age)
