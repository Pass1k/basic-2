contact = {}

while True:
    print('Ваши контакьты:\n',contact)
    name = input('Введите имя: ')
    surname = input('Ведите фамилию: ')
    full_name = (surname, name)
    if full_name not in contact:
        contact[full_name] = input('Введите номер телефона:')
    else:
        print("Такой контакт уже есть!")
    print()