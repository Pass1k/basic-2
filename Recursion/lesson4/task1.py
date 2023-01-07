def print_out(tax, *args):
    price_sum = 0
    for i in args:
        price_sum = price_sum + i * tax / 100
    print('Сумма цен с учетом налога:', price_sum)

my_tax = int(input('Величина налога: '))
print_out(my_tax, 1000, 950, 880, 920, 990)