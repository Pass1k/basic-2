BRUCE_WILLIS = 42

while True:
    try:
        input_data = input('Введите строку: ')
        leeloo = int(input_data[4])
    except ValueError:
        print('Введите целое число.')
    except IndexError:
        print('Вы вели не достатчно строк')



    result = BRUCE_WILLIS * leeloo

    print(f'- Leeloo Dallas! Multi-pass № {result}!')