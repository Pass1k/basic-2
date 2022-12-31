def caesar_cipher(str, user_shift):
    char_list = [(letters[(letters.index(sym) + user_shift) % 33] if sym != ' ' else ' ') for sym in str]
    new_str = ''
    for i in char_list:
        new_str += i
    return new_str

letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
input_str = input('Введите строку: ').lower()
shift = int(input('Введите сдвиг: '))

output_str = caesar_cipher(input_str, shift)

print('Зашифрованная строка:', output_str)