site = {
    'html': {
        'head': {
            'title': 'Куплю/продам {} недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на {}',
            'div': 'Купить',
            'p': 'Продать'
        }
    }
}

def new_site(data_site, tamplate1, teg):
    if isinstance(tamplate1, dict):
        if teg in tamplate1:
            result = tamplate1[teg] = tamplate1[teg].format(data_site)
            return result
        for i_kay, i_value in tamplate1.items():
            result = new_site(data_site, i_value, teg)
            if result is not None:
                return


def redakt_site(tamplate):
    name_produkt = input('Введите название продукта для нового сайта: ')
    temp = tamplate.copy()
    new_site(name_produkt, temp, 'title')
    new_site(name_produkt, temp, 'h2')
    print('tamplate', tamplate, '\n')
    print('temp', temp, '\n')


count_site = int(input('Cколько будет сайтов: '))
for i in range(count_site):
    redakt_site(site)
