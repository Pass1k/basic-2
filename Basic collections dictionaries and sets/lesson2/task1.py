small_storage = {
    'гвозди': 5000,
    'шурупы': 3040,
    'саморезы': 2000
}

big_storage = {
    'доски': 1000,
    'балки': 150,
    'рейки': 600
}

item = input('Введите название товара: ')

if item in big_storage:
    print(f'Количество {item}:', big_storage[item])
else:
    print(big_storage.get(item))

# big_storage.update(small_storage)
# for i in big_storage:
#     print(i, '-', big_storage[i])