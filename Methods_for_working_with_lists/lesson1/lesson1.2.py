nums = int(input('Кол-во сотрудников: '))
employers_salary = []

for i in range(1, nums + 1):
    employers_salary.append(int(input(f'Зарплата {i} сотрудника: ')))

for i in employers_salary:
    if i == 0:
        employers_salary.remove(i)

print('Осталось сотрудников:',len(employers_salary))
print('Зарплаты:',employers_salary)

print('Максимальная зп:',max(employers_salary))
print('Минимальная зп:',min(employers_salary))