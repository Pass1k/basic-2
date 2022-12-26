string = list(input('Введите сроку: '))
index = -1
count = 0


for i in string:
    index += 1
    if i == ':':
        string[index] = ';'
        count += 1

text = ''
for i in string:
    text += i

print('Исправленная строка:',text)
print('Кол-во замен:',count)

