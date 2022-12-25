players = ["Артемий", "Борис", "Влад", "Гоша", "Дима", "Евгений", "Женя", "Захар"]

index = -1
second_day = []
for i in players:
    index += 1
    if index % 2 == 0:
        second_day.append(i)

print('Первый день:',second_day)
