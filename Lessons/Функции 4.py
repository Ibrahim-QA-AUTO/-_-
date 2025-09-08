def power(base, exp=2):
    return base ** exp

print(power(5, 23))

def greet(name, greeting="Привет"):
    return (f"{name}, {greeting}!")

print(greet("Сергей", "Добро пожаловать"))

def rectangle_area(a=1, b=1):
    return a * b

print(rectangle_area(5, 6))

def compare_strings(s1, s2, ignore_case=True, ignore_spaces=True):
    if ignore_case:
        s1, s2 = s1.lower(), s2.lower()
    if ignore_spaces:
        s1, s2 = s1.strip(), s2.strip()
    return s1 == s2

print(compare_strings("ffffff", "FFFFFff"))

def append_to_list(value, lst=None):
    if lst is None:
        lst = []
    lst.append(value)
    return lst

print(append_to_list([22,33,44], [22,33,444,555]))
