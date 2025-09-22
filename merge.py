
dict1 = {"ranger": "rover", "bmw": "swift"}
dict2 = {"bus": "car"}
dict1.update(dict2)
print(dict1)


n = 15
d = {}
for x in range(1, n + 1):
    d[x] = x * x
print(d)


car = {"ranger": 3, "rover": 4, "bmw": 5}
total = 0
for i in car.values():
    total += i
print("sum:", total)


car = {"ranger": 3, "rover": 4, "bmw": 5}
product = 1
for i in car.values():
    product *= i
print("product:", product)
