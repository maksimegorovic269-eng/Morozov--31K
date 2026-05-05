# Задание 10
# Класс Employee со слотами и методом увеличения зарплаты

class Employee:
    __slots__ = ("name", "salary")

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def increase_salary(self, percent):
        self.salary += self.salary * percent / 100


employee = Employee("Иван", 50000)
print("Зарплата до увеличения:", employee.salary)

employee.increase_salary(10)
print("Зарплата после увеличения:", employee.salary)
