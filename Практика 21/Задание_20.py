# Задание 20
# Класс Student со слотами, списком оценок и средним баллом

class Student:
    __slots__ = ("name", "age", "grades")

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []

    def add_grade(self, value):
        self.grades.append(value)

    def average(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)


student1 = Student("Иван", 18)
student1.add_grade(5)
student1.add_grade(4)
student1.add_grade(5)

student2 = Student("Анна", 19)
student2.add_grade(4)
student2.add_grade(4)
student2.add_grade(5)

student3 = Student("Олег", 18)
student3.add_grade(3)
student3.add_grade(4)
student3.add_grade(4)

print(student1.name, "средний балл:", round(student1.average(), 2))
print(student2.name, "средний балл:", round(student2.average(), 2))
print(student3.name, "средний балл:", round(student3.average(), 2))

# Проверка: новые атрибуты добавлять нельзя
try:
    student1.group = "ИС-31"
except AttributeError as error:
    print("Нельзя добавить новый атрибут:", error)
