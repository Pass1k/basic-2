from math import factorial, pow


def calc(data):
    return pow((factorial(data) / pow(data, 3)), 10)


print(calc(10))
