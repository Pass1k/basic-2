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


def find_kay(struct, kay):
    if kay in struct:
        return struct[kay]

    for sub_struct in struct.values():
        if isinstance(sub_struct, dict):
            result = find_kay(sub_struct, kay)
            if result:
                break
    else:
        result = None

    return result


user_kay = input('Какой ключ ищем? ')
value = find_kay(site, user_kay)
if value:
    print(value)
else:
    print('Нету')


