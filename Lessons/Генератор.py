N = 22
a = [x ** 2 for x in range(1, N)]
print(a)


b = [x for x in range(-10, 10) if x % 2 == 0]
print(b)

# d_inp = input("Введите числа: ")
# a = [int(d) for d in d_inp.split()]
# print(a)

list1 = ["ww", "ewewq", "ewqdas"]
g = [len(g) for g in list1]
print(g)

numbers = list(range(1, 21))                  # список от 1 до 20
numbers1 = " ".join(str(n) for n in numbers)  # строка "1 2 3 ... 20"
numbers = ["четное" if x % 2 == 0 else "нечетное" for x in range(1, 21)]
print(numbers)

