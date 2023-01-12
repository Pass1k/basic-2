def Move(n, s, f):
    if n == 1:
        print('1', s, f)
    else:
        tmp = 6 - s - f
        Move(n - 1, s, tmp)
        print(n, s, f)
        Move(n - 1, tmp, f)


n = int(input('Введите количество дисков: '))

Move(n, 1, 3)
