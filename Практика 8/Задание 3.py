class Worker:
    def work(self):
        print("Working...")

class Teacher(Worker):
    def work(self):
        print("Teaching...")

class Programmer(Worker):
    def work(self):
        print("Coding...")

# Пример использования
staff = [Worker(), Teacher(), Programmer()]
for person in staff:
    person.work()