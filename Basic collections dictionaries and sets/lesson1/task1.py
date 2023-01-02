num = int(input('Введите целое число: '))

result = dict()

for i in range(1, num + 1):
    result[i] = i ** 2

print(result)