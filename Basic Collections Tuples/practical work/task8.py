contacts = {}

def adding():
    name = input('Введите имя и фамилию нового контакта (через пробел): ').split()
    full_name = tuple(name)
    if full_name not in contacts:
        contacts[full_name] = int(input('Введите номер телефона: '))
    else:
        print('Такой человек уже есть в контактах.')
    print('Текущий словарь контактов:', contacts)

def looking():
    look_for = input('Введите фамилию для поиска: ')
    for k, v in contacts.items():
        if k[1] == look_for:
            names = ' '.join(k)
            print(names, v)
        else:
            print('Нету такого человка в контаках!')
            break

while True:
    choose = int(input("Введите номер действия:\n1. Добавить контакт\n2. Найти человека\n"))
    if choose == 1:
        adding()
    elif choose == 2:
        looking()
    else:
        print('Вы ввели не правильно')


