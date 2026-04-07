class Worker:
    def work(self):
        print("Working...")

class Teacher(Worker):
    def work(self):
        print("Teaching...")

def excited(func):
    def wrapper():
        print("Let's go!")
        func()
    return wrapper

t = Teacher()
t.work = excited(t.work)
t.work()