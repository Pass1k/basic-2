import math

r = int(input('Введите радиус: '))
h = int(input('Ввдеите высоту: '))

def side_full(radidus, height):
    side = 2 * math.pi * radidus * height

    full = side +  2 * math.pi * radidus ** 2

    return side, full

bot_area, full_are = side_full(r, h)
print('Площадь боковой поверхности:', round(bot_area, 2))
print('Полная площадь:', round(full_are, 2))