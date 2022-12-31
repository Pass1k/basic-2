path = input('Путь к файлу: ')

disk = input('На каком диске должен лежать файл: ')
file_type = input('Требуемое расширение файла: ')

if not path.startswith(disk):
    print('Ошибка')
elif not path.endswith(file_type):
    print('Ошибка')
else:
    print('Путь корректен!')