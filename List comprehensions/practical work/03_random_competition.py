import random

first_team = [round(random.uniform(5.00, 10.00), 2) for _ in range(20)]
second_team = [round(random.uniform(5.00, 10.00), 2) for _ in range(20)]

winner = [first_team[x] if first_team[x] > second_team[x] else second_team[x] for x in range(20)]

print('Первая команда:', first_team)
print('Вторая команда:', second_team)
print('Победители тура:', winner)
