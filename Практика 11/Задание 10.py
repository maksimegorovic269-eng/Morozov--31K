class Calculator:
    def calculate(self, x, y=None):
        if y is None:
            return x ** 2
        return x + y

def log_call(func):
    def wrapper(*args, **kwargs):
        print("Function called")
        return func(*args, **kwargs)
    return wrapper

class AdvancedCalculator(Calculator):
    def calculate(self, x, y=None):
        result = super().calculate(x, y)
        return result + 10

calc = AdvancedCalculator()
calc.calculate = log_call(calc.calculate)

print(calc.calculate(5))
print(calc.calculate(2, 3))