# Задание 2
# Класс Animal со слотами

class Animal:
    __slots__ = ("type", "weight")


animal = Animal()
animal.type = "Кот"
animal.weight = 4.5

print("Тип животного:", animal.type)
print("Вес:", animal.weight)

# Попытка добавить новый атрибут color вызовет ошибку AttributeError,
# потому что в __slots__ разрешены только type и weight.
try:
    animal.color = "Черный"
except AttributeError as error:
    print("Ошибка:", error)
    print("Новый атрибут добавить нельзя, так как он не указан в __slots__.")
