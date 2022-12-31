text = input('Введите строку: ')

upper = 0
lower = 0
for i in text:
    if i.isupper():
        upper += 1
    elif i.islower():
        lower += 1

if upper > lower:
    print('Результат:', text.upper())
else:
    print('Результат:', text.lower())