#Тут у меня два способа решение
first_list = []
second_list = []


for i_one in range(3):
    first_list.append(int(input(f'Введите {i_one + 1}-е число для первого списка: ')))
print('Первый список:',first_list)

for i_two in range(7):
    second_list.append(int(input(f'Введите {i_two + 1}-е число для первого списка: ')))
print('Второй список:',second_list)

first_list.extend(second_list)

unique = []

for number in first_list:
    if number in unique:
        continue
    else:
        unique.append(number)

print(f'Новый первый список с уникальными элементами:{unique}')
