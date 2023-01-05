def looking_for(seria, number):
    name = seria, number
    if name in data:
        print(data[name])
    else:
        print('Такого человека нет')

data = {
    (5000, 123456): ('Иванов', 'Василий'),
    (6000, 111111): ('Иванов', 'Петр'),
    (7000, 222222): ('Медведев', 'Алексей'),
    (8000, 333333): ('Алексеев', 'Георгий'),
    (9000, 444444): ('Георгиева', 'Мария')
}

seri = int(input('Ввдите серию: '))
numbers = int(input('Введите номер: '))

looking_for(seri, numbers)