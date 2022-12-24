workers = []
numbers_of_workers = int(input('Кол-во сотрудников в офисе: '))

for i in range(numbers_of_workers):
    workers.append(int(input('ID сотрудника: ')))

not_here = int(input('Кого ищем? '))

if not_here in workers:
    print('Сотрудник на месте.')
else:
    print('Сотрудник не работает!')