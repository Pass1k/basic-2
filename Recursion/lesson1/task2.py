import math


def power(a, n):
    return math.pow(a, n)


float_num = float(input('Введите вещественное число: '))
int_num = int(input('Введите степень числа: '))

print(float_num, '**', int_num, '=', power(float_num, int_num))
