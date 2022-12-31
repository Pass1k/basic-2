name = input('Введите имя: ')
borrow = int(input('Введите долг: '))

text = '{name}! {name}, привет! Как дела, {name}? Где мои {money} рублей? {name}!'.format(
    name = name,
    money = borrow
)

print(text)