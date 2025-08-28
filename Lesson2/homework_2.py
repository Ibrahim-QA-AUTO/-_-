


# 1. Работа с целыми и вещественными числами
a = 1
b = 2
x = 1.1
y = 2.2
print(a,b,y,x)
print(type(a))
print(type(b))
print(type(x))
print(type(y))


# 2. Основные арифметические операции
num1 = 1
num2 = 2
print(num1 + num2, num1 - num2, num1 * num2, num1 / num2, num1 // num2, num1 % num2, num1 ** num2)



# 3. Особенности работы с делением
a = 10
b = 3
print(a / b, a // b, a % b)

a = -10
b = -3
print(a / b, a // b, a % b)

# 4. Работа с приоритетом операторов
print(5 + 3 *2, (5 + 3) * 2, 10 / 2 ** 2)


# 5. Использование сокращенных операторов
count = 10
count += 5
count -= 3
count *= 2
count /= 4
print(count)


# 1. Создание строк
s1 = "Python"
s2 = 'Программирование'
print(s1, s2)
s3 = """многострочная\nстрока
"""
print(s3)
empty = ""
print(len(empty))


# 2. Конкатенация строк
first_name = "Иван"
last_name = "Петров"
full_name = first_name + " " + last_name
print(full_name)

# 3. Преобразование типов
s = "Возраст: "
age = 25
total = s + str(age)
print(total)


# 4. Дублирование строк
print("ха " * 5)
# print("xa " * 2.5) выдает ошибку

# 5. Длина строки
text = "Привет, мир!"
print(len(text))
empty = ""
print(len(empty))

# 6. Проверка вхождения подстроки
sentence = "Я изучаю Python"
print("Python" in sentence)
print("Java" in sentence)

# 7. Сравнение строк
a = "apple"
b = "banana"
print(a == b, a != b, a < b, a > b, a <= b, a >=b)


# 8. Код символов
print(ord("А"))
print(ord("а"))
print(ord("Я"))
