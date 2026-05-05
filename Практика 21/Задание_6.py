# Задание 6
# Класс Student со слотами и методом изменения оценки

class Student:
    __slots__ = ("name", "grade")

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def change_grade(self, new_grade):
        self.grade = new_grade


student = Student("Алексей", 4)
print("Студент:", student.name)
print("Оценка до изменения:", student.grade)

student.change_grade(5)
print("Оценка после изменения:", student.grade)
