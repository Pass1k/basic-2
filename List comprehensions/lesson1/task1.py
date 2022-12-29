x1 = int(input('Левая граница: '))
y1 = int(input('Правая граница: '))

first_list = [x ** 3 for x in range(x1, y1 + 1)]
second_list = [x ** 2 for x in range(x1, y1 + 1)]

print(f'Список кубов чисел в диапазоне от {x1} до {y1}:',first_list)
print(f'Список квадратов чисел в диапазоне от {x1} до {y1}:',second_list)