import random

nums_1 = [29, 17, 10, 15, 13, 22, 12, 22, 7, 24, 26, 3, 11, 2, 3, 16, 19, 21, 2, 3, 8, 27, 2, 17, 2, 20, 12, 21, 3, 1]
nums_2 = [16, 21, 30, 24, 5, 7, 23, 13, 11, 5, 21, 5, 19, 9, 12, 9, 15, 16, 29, 8, 16, 1, 22, 15, 16, 9, 1, 13, 21, 21]

nums_1 = set(nums_1)
nums_2 = set(nums_2)

print(type(nums_1))
print(type(nums_2))
print('Без повторяющиеся элементы:', nums_1)
print('Без повторяющиеся элементы:', nums_2)

nums_1.remove(min(nums_1))
nums_2.remove(min(nums_2))
print(nums_1)
print(nums_2)
nums_1.add(random.randint(100, 200))
nums_2.add(random.randint(100, 200))
print(nums_1)
print(nums_2)
print('Вывести все элементы множеств (объединение):', nums_1.union(nums_2))
print('Вывести только общие элементы (пересечение):', nums_1.intersection(nums_2))
print('Вывести элементы, входящие в nums_2, но не входящие в nums_1.', nums_2.difference(nums_1))