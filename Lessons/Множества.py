a = {1, 2, 3, 4, 5}
print(type(a))
a = set(a)
print(type(a))
a.add(6)
print(a)
a.add(3)
print(a)

cities = ["Москва", "Тюмень", "Калуга", "Москва", "Омск", "Калуга", "Тверь"]
cities = set(cities)
print(cities)
print(type(cities))
print(len(cities))

b = set([x for x in range(1, 11)])
print(type(b))
print(b)
b.remove(5)
b.discard(15)
print(b)

c = "abrakadabra"
c = set(c)
print(c)
print(len(c))

f = set()
f.add(10)
f.add("Hello")
f.update((1,2,3))
print(f)

