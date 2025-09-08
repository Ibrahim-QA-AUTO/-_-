def sum_all(*args):
    return sum(args)

print(sum_all(1,2,3,4,5,6))

def print_info(name, age, **kwargs):
    print(f"Имя: {name}")
    print(f"Возраст: {age}")
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")

# Вызов
print_info("Сергей", 25, религия="Мусульманин", семья="Женат")

def merge_lists(*lists):
    full_list = []
    for lst in lists:
        full_list += lst   # расширяем общий список
    return full_list

print(merge_lists([1,2],[22,33],[22,333]))

def merge_dicts(*dicts):
    full_dict = {}
    for dict1 in dicts:
        full_dict.update(dict1)
    return full_dict

d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
d3 = {"c": 5, "d": 6}

print(merge_dicts(d1, d2, d3))

def unpack_list(lst):
    first, *rest = lst
    return first, rest

print(unpack_list([10, 20, 30, 40]))
print(type(unpack_list([10, 20, 30, 40])))