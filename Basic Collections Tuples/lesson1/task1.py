import random

tuple_1 = [random.randint(0, 5) for i in range(10)]
tuple_2 = [random.randint(-5, 0) for i in range(10)]

print(tuple(tuple_1))
print(tuple(tuple_2))

for i in tuple_2:
    tuple_1.append(i)
tuple_1 = tuple(tuple_1)

print(tuple_1, 'Количесвто 0-ей:', tuple_1.count(0))
print(tuple(tuple_2))
