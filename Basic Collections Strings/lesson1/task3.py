while True:
    tamplate = input('Введите шаблон поздравления, в шаблоне можно использовать конструкцию {name} и {age}: ')

    if 'name' in tamplate and 'age' in tamplate:
        break
    print('Ошибка: отсутствует одна или две конструкции.')

names_list = input('Список людей через запятую: ').split(', ')
ages_str = input('Возраст людей через пробел: ')
ages = [int(i_number) for i_number in ages_str.split()]

for i in range(len(names_list)):
    print(tamplate.format(
        name = names_list[i],
        age = ages[i]
    ))

people = [
    ' '.join([names_list[i_man], str(ages[i_man])])
    for i_man in range(len(names_list))
]

people_str = ', '.join(people)
print('\nИменинники:', people_str)