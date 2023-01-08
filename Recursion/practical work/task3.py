def find(number):
    if number == 1 or number == 2:
        return 1
    return find(number - 1) + find(number - 2)

num = int(input('Введите позицию числа в ряде Фибоначчи: '))
print('Число:', find(num))