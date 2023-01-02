contact = dict()
while True:
    print('Текущие контакты на телефоне:\n', contact)
    name = input('Введите имя: ')

    if name not in contact:
        number = int(input('Введите номер телефона: '))
        contact[name] = number
    else:
        print('Ошибка: такое имя уже существует.')
    print()
