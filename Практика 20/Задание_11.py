# Задание 11 – Email-дескриптор

class EmailDescriptor:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if "@" not in value:
            raise ValueError("Email должен содержать символ @")
        instance.__dict__[self.name] = value


class User:
    email = EmailDescriptor()


user = User()
user.email = "test@mail.com"
print(user.email)
