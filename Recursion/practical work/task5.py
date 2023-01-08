def fact(x):
    if x == 1:
        return 1
    return fact(x - 1) * x

y = int(input('Введите число: '))
x = (fact(y) / y ** 3) ** 10

print(round(x, 5))