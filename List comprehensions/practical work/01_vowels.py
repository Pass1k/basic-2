letters = 'аоиеёэыуюя'

text = input('Введите текст: ').lower()

letters_in_text = [char for char in text if char in letters]

print('Список гласных букв:', letters_in_text)
print('Длина списка:', len(letters_in_text))
