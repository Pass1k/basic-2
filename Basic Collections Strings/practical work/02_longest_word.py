text = input('Введите строку: ').split()

longest = 0
word = ''
for i in text:
    if len(i) > longest:
        longest = len(i)
        word = i

print('Самое длинное слово:', word)
print('Длина этого слова:', longest)
