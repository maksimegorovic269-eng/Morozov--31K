# Задание 1
# Класс Person с использованием __slots__

class Person:
    __slots__ = ("name", "age")


person = Person()
person.name = "Иван"
person.age = 20

print("Имя:", person.name)
print("Возраст:", person.age)
