def check_age(age):
    try:
        if age < 0:
            raise ValueError
        return "OK"
    except ValueError:
        return "Invalid age"

# Пример
print(check_age(20))
print(check_age(-5))