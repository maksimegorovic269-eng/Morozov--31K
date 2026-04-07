def logger(func):
    def wrapper():
        print(f"Calling {func.__name__}")
        func()
    return wrapper

@logger
def say_hello():
    print("Hello!")

say_hello()