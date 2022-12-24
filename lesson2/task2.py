n = int(input('Кол-во чисел в списке: '))
numbers = []

for i in range(1,n + 1):
    numbers.append(int(input(f'Введите {i} число: ')))

divider = int(input('Введите делитель: '))
index = 0
sum_indexes = 0

for number in numbers:
    if number % divider == 0:
        print(f"Индекс числа {number}: {index}")
        sum_indexes += index
    index += 1

print("Сумма индексов:", sum_indexes)



