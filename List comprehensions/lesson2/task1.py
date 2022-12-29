start = int(input('Начальная число: '))
stop = int(input('Конечное число: '))

list = [x for x in range(start,stop) if x % 2 == 0]
print(list)