
# Задачи на input() и print()


# 1. Простая работа с print()
print("Привет, мир!")
print(5, 10, 15)
print(10 + 25)

# 2. Использование параметров sep и end в print()
print(1, 2, 3, sep=" & ")
print("Python ", end="")
print("лучший язык")


# 3. Форматированный вывод с F-строками
x, y = 3.14, -8
print(f"Координаты точки: x = {x}; y = {y}")
name = input()
age = input()
print(f"Имя: {name}, Возраст: {age}")

# 4. Работа с input()
name = input()
print(f"Привет, {name}!")

# 5. Преобразование типов
a = float(input())
b = float(input())
print(a + b)
c = int(input())
print(c ** 2)

# 1. Основы булевой логики
print(5 > 3, 10 < 2, 7 == 7, 6 !=8, 4 >= 4, 9 <= 3, sep="\n")
res = 8 > 12
print(res)
print(type(res))


# 2. Проверка четности и кратности числа
x = 15
print(x % 2 == 0)
print(x % 5 == 0)
print(x % 3 == 0 and x % 5 == 0)

# 3. Работа с логическими операторами (and, or, not)
y = 4.5
print(y >= 1 and y <= 10)
print(0 <= y <= 5 or 10 <= y <= 15)
print(not y < 5)

# 4. Приоритет логических операций

# Вычисли и выведи результаты следующих выражений:
# True or False and False = True
# not False and True = True
# False or not True and True = False
# not (10 > 5 or 3 < 1) = False
#
# 5. Приведение типов к bool
print(bool(0)) # False
print(bool(-5)) # True
print(bool(3.14)) # True
print(bool("")) # False
print(bool("Python")) # True
print(bool(" ")) # True

# 6. Дополнительное задание
n = 111
print(n > 0, n % 2 == 0, n % 3 == 0, sep="\n")

# 1. Доступ к символам по индексу.
s = "Программирование"
print(s[0])
print(s[-1])
print(s[2])
print(s[-2])

# 2. Обращение к символам с проверкой границ
# print(s[100]) # выведет ошибку о том, что мы за границей индекса
print(s[len(s)-1])   # последний символ (эквивалентно s[-1])

# 3. Создание срезов
new_s = s[:6]
print(new_s)
new_s2 = s[-5:]
print(new_s2)
new_s3 = s[2:7]
print(new_s3)
print(s[::2])
print(s[::-1])


# 4. Работа с шагом в срезах
print(s[::3])
print(s[::-2])

# 5. Проверка неизменяемости строк
# s[0] = "п" ошибка в том, что строка неизменяемый тип данных, так нельзя делать
s = "программирование"
s2 = "П" + s[1:]
print(s2)

# 6. Дополнительное задание
word = "abcdefgh"
word2 = word[2:5]
print(word2)
print(word[::-1])
print(word[1:-1])
