dogs_count = int(input('Введите кол-во сабак: '))
dogs_point = []

for i in range(1, dogs_count + 1):
    dogs_point.append(int(input(f'Введите очко {i}-й сабаки: ')))

if dogs_point:
    maximum = dogs_point[0]
    minimum = dogs_point[0]

    max_index = 0
    min_index = 0

    for index, i in enumerate(dogs_point):

        if maximum < i:
            maximum = i
            max_index = index

        if minimum > i:
            minimum = i
            min = index

    print('Максимальное число в списке:', maximum)
    print('Минимальное число в списке:', minimum)

    print(dogs_point)
    dogs_point[min_index], dogs_point[max_index] = dogs_point[max_index], dogs_point[min_index]
    print(dogs_point)

