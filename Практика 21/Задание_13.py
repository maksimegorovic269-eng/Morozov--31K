# Задание 13
# Наследование классов со слотами

class Person:
    __slots__ = ("name",)

    def __init__(self, name):
        self.name = name


class Student(Person):
    __slots__ = ("grade",)

    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade


student = Student("Анна", 5)

print("Имя:", student.name)
print("Оценка:", student.grade)
