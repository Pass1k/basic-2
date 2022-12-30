import random

count = int(input('Количество чисел в списке: '))
random_list = [random.randint(0, 2) for i in range(count)]
new_list = [x for x in random_list if x != 0]

print('Список до сжатия:', random_list)
print('Список после сжатия:', new_list)
