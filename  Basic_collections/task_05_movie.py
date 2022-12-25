films = [
    'Крепкий орешек',
    'Назад в будущее',
    'Таксист',
    'Леон',
    'Богемская рапсодия',
    'Город грехов',
    'Мементо',
    'Отступники',
    'Деревня',
]

count = int(input('Сколько фильмов хотите добавить? '))
favorite_films = []

for i in range(1, count + 1):
    name = input('Введите название фильма: ')
    if name in films:
        favorite_films.append(name)
    else:
        print(f'Ошибка: фильма {name} у нас нет :(')

print('Ваш список любимых фильмов:',favorite_films)
