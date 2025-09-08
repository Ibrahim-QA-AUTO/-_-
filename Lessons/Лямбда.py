square = lambda x: x ** 2
print(square(2))

is_double = lambda x: x % 2 == 0
print(is_double(54))

numbers = [1, 2, 3, 4]
square2 = list(map(lambda x: x ** 2, numbers))

print(square2)

nums = [-3, 0, 5, -8, 10]
positive = list(filter(lambda x: x > 0, nums))
print(positive)

def sort_by_last_letter(words):
    return sorted(words, key=lambda word: word[-1])

words = ["banana", "apple", "cherry"]
print(sort_by_last_letter(words))