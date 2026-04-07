def check_positive(func):
    def wrapper(*args):
        if any(a < 0 for a in args):
            print("Error")
        else:
            func(*args)
    return wrapper

@check_positive
def multiply(a, b):
    print(a * b)

multiply(3, 4)
multiply(3, -1)
