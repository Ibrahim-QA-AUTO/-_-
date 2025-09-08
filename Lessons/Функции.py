def greet(name):
    print(f"Привет, {name}! Добро пожаловать!")

greet("Сергей")

def square(num):
    print(f"Квадрат вашего числа {num} равен {num**2}")

square(223)

def sum_numbers(a, b):
    print(f"Сумма чисел равна {a + b}")

sum_numbers(22, 44)

def is_even(num):
    return num % 2 == 0

print(is_even(332))

def repeat_string(text, times):
    print((text + "\n") * times)

repeat_string("пупупупупупу", 35)
