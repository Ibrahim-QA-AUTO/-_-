i = [1, 3, 5, 6, 7]
i = iter(i)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))

str = "hello"
it = iter(str)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

def is_iterable(obj):
    try:
        iter(obj)  # Пробуем создать итератор
        return True
    except TypeError:  # Если возникает ошибка, значит, объект не итерируемый
        return False

# Тестируем функцию
print(is_iterable([1, 2, 3]))  # True (список)
print(is_iterable("abc"))      # True (строка)
print(is_iterable(42))         # False (число)
print(is_iterable({1, 2, 3}))  # True (множество)
