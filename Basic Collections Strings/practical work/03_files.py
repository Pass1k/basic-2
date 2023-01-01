file_name = input('Название файла: ')
extensions = ('.txt', '.docx')

if file_name.startswith(('@', '№', '$', '%', '^', '&', '*', '(', ')')):
    print('Ошибка: название начинается на один из специальных символов')
elif not file_name.endswith(('.txt', '.docx')):
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx')
else:
    print('Файл назван верно.')
