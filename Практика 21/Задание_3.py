# Задание 3
# Сравнение класса со слотами и класса без слотов

class WithSlots:
    __slots__ = ("name",)


class WithoutSlots:
    pass


obj1 = WithSlots()
obj1.name = "Объект со слотами"

obj2 = WithoutSlots()
obj2.name = "Объект без слотов"

print(obj1.name)
print(obj2.name)

try:
    obj1.age = 20
except AttributeError as error:
    print("Для объекта со слотами нельзя добавить новый атрибут:", error)

obj2.age = 20
print("Для объекта без слотов новый атрибут добавлен:", obj2.age)

print("Вывод: __slots__ ограничивает список доступных атрибутов объекта.")
