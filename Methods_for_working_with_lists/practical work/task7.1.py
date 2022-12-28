skate_sizes = []
legs_sizes = []

count_skate = int(input('Кол-во коньков: '))

for i in range(count_skate):
    query = int(input(f'Размер {i + 1}-й пары: '))
    skate_sizes.append(query)
print()

count_people = int(input('Кол-во людей: '))
for i in range(count_people):
    query = int(input(f'Размер ноги {i + 1}-го человека:'))
    legs_sizes.append(query)

count_people_can_take = 0
for i_legs in legs_sizes:
    for i_skate in skate_sizes:
        if i_legs == i_skate:
            legs_sizes.remove(i_skate)
            count_people_can_take += 1

print(f'Наибольшее кол-во людей, которые могут взять ролики: {count_people_can_take}')
