site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


def find_kay(struct, kay, depth):
    if depth == 1:
        if kay in struct:
            return struct[kay]
    if depth > 1:
        for sub_struct in struct.values():
            if isinstance(sub_struct, dict):
                result = find_kay(sub_struct, kay, depth - 1)
                if result:
                    break
        else:
            result = None
        return result


user_kay = input('Какой ключ ищем? ')
search_depth = int(input('Введите глубину поиска: '))
value = find_kay(site, user_kay, search_depth)


if value:
    print(value)
else:
    print('Такого ключа в струкутре сайта нет.')