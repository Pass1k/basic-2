x = input('x: ')
y = input('y: ')

try:
    x = int(x)
    y = int(y)
    res = x/y
except ZeroDivisionError:
    res = 'Деление на ноль'
print(res)