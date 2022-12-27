first_class = []
second_class = []
together = []

for i in range(160,176 + 1,2):
    first_class.append(i)
    together.append(i)
print('Первый класс:',first_class)

for i in range(162,180 + 1, 3):
    second_class.append(i)
    together.append(i)
print('Второй класс:',second_class)

for i_min in range(len(together)):
    for current in range(i_min, len(together)):
        if together[current] < together[i_min]:
            together[current], together[i_min] = together[i_min], together[current]

print('Отсортированный список учеников:',together)

