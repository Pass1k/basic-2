def print_out(tax, *args, **kwargs):
    price_sum = 0
    for i in args:
        price_sum = price_sum + i * tax / 100
    print('Сумма цен с учетом налога:', price_sum)

    for k, v in kwargs.items():
        print('{}: {}'.format(k, v))

my_tax = int(input('Величина налога: '))
print_out(my_tax, 1000, 950, 880, 920, 990,
          year = 2023, doc_type = 'Report', id = 202000)