# Задание 15
# Класс BankAccount со слотами, пополнением и снятием

class BankAccount:
    __slots__ = ("balance",)

    def __init__(self, balance=0):
        if balance < 0:
            raise ValueError("Начальный баланс не может быть отрицательным")
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной")
        if self.balance - amount < 0:
            raise ValueError("Недостаточно средств")
        self.balance -= amount


account = BankAccount(1000)
print("Начальный баланс:", account.balance)

account.deposit(500)
print("Баланс после пополнения:", account.balance)

account.withdraw(300)
print("Баланс после снятия:", account.balance)

try:
    account.withdraw(2000)
except ValueError as error:
    print("Ошибка:", error)
