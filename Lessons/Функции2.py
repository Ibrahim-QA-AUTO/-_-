def get_sqrt(x):
    res = None if x < 0 else x ** 0.5
    return res  # Возвращаем результат

print(get_sqrt(49))

def add(a, b):
    return a + b

print(add(1,3))

def is_positive(num):
    if num > 0:
        return True


print(is_positive(-22))

def get_max(a, b, c):
    return max(a,b,c)

print(get_max(2,5,88))

def reverse_string(text):
    text = text[::-1]
    return text

print(reverse_string("Абобааааааа"))

