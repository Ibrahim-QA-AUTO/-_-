
# 1. Работа с регистром
s = "Python для автоматизации"
s = s.upper()
print(s)
s = s.lower()
print(s)

# 2. Подсчет вхождений подстроки
msg = "абракадабра"
total = msg.count("ра")
print(total)
total = msg.count("а", 3)
print(total)

# 3. Поиск подстроки
print(msg.find("ка"))
print(msg.rfind("а"))
print(msg.find("xyz")) # выведет -1


# 4. Замена подстроки
text = "Я изучаю Java"
new_text = text.replace("Java", "Python")
print(new_text)
print(new_text.replace(" ", ""))

# 5. Проверка содержимого строки
print("Python".isalpha())
print("12345".isdigit())
print("123abc".isdigit())

# 6. Дополнение строк
code = "42"
print(code.rjust(5, "0"))
print(text.ljust(10, "*"))

# 7. Разбиение строк
string1 = "яблоко, груша, банан"
new_string = string1.replace("," , "")  # тут я забыл, что можно в split передать , и она уйдет
fruit1, fruit2, fruit3 = new_string.split()
print(fruit1)
print(fruit2)
print(fruit3)
str2 = "Python;Java;C++"
lan1, lan2, lan3 = str2.split(";")
print(lan1)
print(lan2)
print(lan3)


# 8. Объединение списка в строку
list1 = ["Привет", "мир", "!"]
print(' '.join(list1))
list2 = ["apple", "banana", "cherry"]
print(', '.join(list2))

# 9. Удаление пробелов
print(" Python".lstrip())
print("Python ".rstrip())
print(" Python ".strip())

# 10. Дополнительное задание
text = "программирование"
text = text[0].upper() + text[1:]
print(text)
print(text.count("р"))
print(text.find("и"))
print(text[::-1])

# 1. Перевод строки
text = "Hello\nPython"
print(text)
# перешел на новую строку из-за символа \n

# 2. Горизонтальная табуляция
t = "Python\tAutomation"
print(t) # это длинный пробел

# 3. Экранирование символов
path = "C:\new\test.txt"
print(path) # символы применились \n дало переход на новую строку, а \t длинный пробел
print("Марка вина \"Ягодка\"")

# 4. Сырые (raw) строки
path = r"C:\new\test.txt" # сырая не взаимодействует со спецсимволами, просто выводит их как текст

# 5. Использование разных спецсимволов
s = "Hello\b World"
print(s)  # буква "o" удалилась, \b удаляет символ перед собой либо не выводит его
s = "Hello\fPython"
print(s) # вставился символ  на вывод

# 1. Формирование строк через конкатенацию
name = "Ibrohim"
age = 27
text = "Меня зовут " + name + ", мне " + str(age) + " лет."
print(text)
# text = "Меня зовут " + name + ", мне " + age + " лет." Ошибка, в строке нельзя int вставлять

# 2. Форматирование строк с .format()
text1 = "Меня зовут {0}, мне {1} лет".format(name, age)
print(text1)
text2 = "Меня зовут {Imya}, мне {Voz} лет".format(Imya = name, Voz = age)
print(text2)
text3 = "Меня зовут {Imya}, мне {Voz} лет".format(Voz = age, Imya = name) # все норм, тут можно менять
print(text3)

# 3. Использование F-строк
city = "Майкоп"
year = 2000
print(f"Сегодня {year}, и я живу в {city}е")
print(f"Через 5 лет будет {year + 5} год")

# 4. Операции внутри F-строк
print(f"Дважды мой возраст: {age*2}")
print(name.upper())

# 5. Дополнительное задание
print("Курс валют: {dollar} доллар = {ruble} рубля.".format(dollar = 1, ruble = 92.5))
print(f"Квадрат числа 7 равен {7**2}.")
