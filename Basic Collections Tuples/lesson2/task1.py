text = input('Введите строку: ')

index = ''
for i, q in enumerate(text):
    if q == '~':
        index += str(i)

print('Ответ:', index)