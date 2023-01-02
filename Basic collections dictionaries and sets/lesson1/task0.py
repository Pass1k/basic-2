phonebook = {
    'Ваня': 87072715907,
    'Петя': 87002002020
}

name = input('Введите имя: ')

if name in phonebook:
    print(phonebook[name])
else:
    print('Ошибка: человек с имненем {0} не найден'.format(name))