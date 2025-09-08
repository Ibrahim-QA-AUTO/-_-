a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

res = a & b
print(res)
print(a | b)
print(a - b)
print(b - a)
print(a ^ b)


X = {10, 20, 30, 40, 50}
Y = {30, 40}

print(Y < X)
print(X > Y)

even_numbers = set([x for x in range(1, 11) if x % 2 == 0])
print(even_numbers)
odd_numbers = set([x for x in range(1, 11) if x % 2 == 1])
print(odd_numbers)
print(even_numbers & odd_numbers)
print(even_numbers | odd_numbers)
print(even_numbers < odd_numbers)

python_students = {"Анна", "Иван", "Мария", "Сергей"}
java_students = {"Иван", "Дмитрий", "Сергей", "Алексей"}
print(python_students & java_students)
print(python_students ^ java_students)
print(python_students | java_students)

text1 = set("программирование")
text2 = set("автоматизация")
print(text1 & text2)
print(text1 - text2)
print(text1 | text2)