a = {x**2 for x in range(1, 11) if x % 2 == 0 }
print(a)

words = ["apple", "banana", "cherry", "apple", "banana", "date", "cherry"]
set(words)
set1 = {x.upper() for x in words}
print(set1)

grades = {"Alice": 85, "Bob": 78, "Charlie": 92, "David": 60, "Eve": 88}
grade_labels = {name: "отлично" if score >= 80 else "удовлетворительно" for name, score in grades.items()}
print(grade_labels)


text = {"Python", "automation", "programming", "testing"}
text = {word: len(word) for word in words}
print(text)

set2 = {x for x in range (1, 6): f**2 for f in range(1, x) }
print(set2)