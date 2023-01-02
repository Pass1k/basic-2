incomes = {
    'apple': 5600.20,
    'orange': 3500.45,
    'banana': 5000.00,
    'bergamot': 3700.56,
    'durian': 5987.23,
    'grapefruit': 300.40,
    'peach': 10000.50,
    'pear': 1020.00,
    'persimmon': 310.00,
}

total = sum(incomes.values())
print(f'Общий доход за год составил {total} рублей')
lowest = min(incomes.values())
lowest_name = ''

for i in incomes:
    if incomes[i] == lowest:
        lowest_name = i

print(f'Самый маленький доход у {lowest_name}. Он составляет {lowest} рублей')
incomes.pop(lowest_name)
print('Итоговый словарь:', incomes)