tuple1 = ([1,2,3,4], True, {"name": "John"}, "Str")
print(tuple1)

nums = (4, 7, 2, 9, 4, 1, 7, 4, 3, 9)
print(nums.count(4))
print(nums.index(7))

lst = ["Python", "Java", "C++", "JavaScript"]
tuple2 = tuple(lst)
print(type(tuple2))

tuple3 = tuple(x for x in range(1, 11))
print(tuple3)
print(tuple3[:3])
print(tuple3[-3:])
print(tuple3[::2])

tuple4 = ([1,2,3,4], {"name": "John"})
tuple4[0].append(5)
print(tuple4)
