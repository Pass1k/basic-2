nums_sum = 0
nums_count = 0

try:
    numbers_file = open('numbers.txt', 'r')
    for i in numbers_file:
        nums_count += 1
        nums_sum += int(i)
    numbers_file.close()
    print('Средний арифматический:', nums_sum / nums_count)
except FileNotFoundError:
    print('Такого файла нету в папке')
except ValueError:
    print('Файл должен содержать целые числа')