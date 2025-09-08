fruits = {
    "banana" : 120,
    "apple" : 50,
    "melon" : 200
}

fruits["mango"] = 100
print(fruits)

grades = {"Анна": 5, "Борис": 4, "Виктор": 3, "Галина": 5, "Дмитрий": 2}

for name, grade in grades.items():
    if grade >= 4:
        print(name)

squares = [x ** 2 for x in range(1, 6)]
print(squares)

capitals = {"Россия": "Москва", "Франция": "Париж", "Германия": "Берлин", "Италия": "Рим"}

# country = input("Введите страну: ")
# print(capitals.get(country))

students = [("Анна", "Python"), ("Борис", "Java"), ("Виктор", "Python"), ("Галина", "C++"), ("Дмитрий", "Python")]
courses = {}

for name, course in students:
    if course not in courses:
        courses[course] = []  # Создаем список, если предмета еще нет
    courses[course].append(name)  # Добавляем студента в список

print(courses)

capitals = {"Россия": "Москва", "Франция": "Париж", "Германия": "Берлин", "Италия": "Рим"}
capitals.setdefault("Белорусь" , "Минск")
print(capitals)

grades = {"Анна": 5, "Борис": 4, "Виктор": 3, "Галина": 5, "Дмитрий": 2}
min_student = min(grades, key=grades.get)
grades.pop(min_student)
print(grades)

students = [["Анна", 20], ["Борис", 22], ["Виктор", 19], ["Галина", 21]]
students = dict.fromkeys([students])
print(students)



