def all_num(num):
    if num < 1:
        return
    all_num(num - 1)
    print(num)

number = int(input('Введите num: '))
all_num(number)