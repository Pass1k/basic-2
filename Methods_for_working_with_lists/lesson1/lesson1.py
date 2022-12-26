zoo = [
    'lion',
    'kangaroo',
    'elephant',
    'monkey'
]

zoo.insert(1, 'bear')

print(zoo)

animal_to_remove = input('Кого убрать?')

if animal_to_remove in zoo:
    zoo.remove(animal_to_remove)


print('Лев сидит в клетке номер',zoo.index('lion') + 1)
print('Обезьяна сидит в клетке номер',zoo.index('monkey') + 1)
print(zoo)

