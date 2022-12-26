words = []
text = ''

word1 = 0
word2 = 0
word3 = 0

for i in range(3):
    words.append(input(f'Введите {i+1} слово: '))

print()
while text != 'end':
    text = input('Слово из текста: ')
    if text in words[0]:
        word1 += 1
    elif text in words[1]:
        word2 += 1
    elif text in words[2]:
        word3 += 1

print()
print('Подсчёт слов в тексте')
print(f'{words[0]}: {word1}')
print(f'{words[1]}: {word2}')
print(f'{words[2]}: {word3}')