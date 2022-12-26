films = [
    'Крепкий орешек', 'Назад в будущее', 'Таксист',
    'Леон', 'Богемская рапсодия', 'Город грехов',
    'Мементо', 'Отступники', 'Деревня',
    'Проклятый остров', 'Начало', 'Матрица'
]

my_films = []

while True:
    print('Ваш текущий топ фильмов:',my_films)
    film_name = input('Название фильма: ')

    if film_name in films:
        command = input('Команды: добавить, вставить, удалить \nВведите команду: ')
        if command == 'добавить':
            my_films.append(film_name)
            print()
        elif command == 'удалить':
            my_films.remove(film_name)
            print()
        elif command == 'вставить':
            place = int(input('На какое место хотите вставить: '))
            my_films.index(film_name, place + 1)
            print()
    else:
        print('Нету такого фильма')