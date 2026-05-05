# Задание 12
# Класс User со слотами и методом изменения пароля

class User:
    __slots__ = ("login", "password")

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def change_password(self, new_password):
        self.password = new_password


user = User("admin", "12345")
print("Логин:", user.login)
print("Старый пароль:", user.password)

user.change_password("qwerty123")
print("Новый пароль:", user.password)
