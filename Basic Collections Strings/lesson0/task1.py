name = input('Имя: ')
order_number = int(input('Номер заказа: '))

the_format = 'Здравствуйте, {name}! Ваш номер заказа: {number}. Приятного дня!'.format(
    name = name,
    number = order_number
)

print(the_format)

