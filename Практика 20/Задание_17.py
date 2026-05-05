# Задание 17 – Кэширование

class CachedDescriptor:
    def __get__(self, instance, owner):
        if "_cached_value" not in instance.__dict__:
            print("Вычисление значения")
            instance.__dict__["_cached_value"] = sum(range(1, 101))
        return instance.__dict__["_cached_value"]


class Test:
    value = CachedDescriptor()


obj = Test()
print(obj.value)
print(obj.value)
print(obj.value)
