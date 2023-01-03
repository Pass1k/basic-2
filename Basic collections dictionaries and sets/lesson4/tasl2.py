text = set(input('Введите строку: '))
result = text & set("0123456789")
new_text = ''
for i in result:
    new_text += i

print('Различные цифры строки:', sorted(new_text))
