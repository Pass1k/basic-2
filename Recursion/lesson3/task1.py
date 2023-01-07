def ask_user(
        quation ='Вы действительно хотите выйти? ',
        complain = "Неверный ввод. Пожалуйста, введите 'да' или 'нет'.",
        retry = 3):
    while retry > 0:
        answer = input(quation)
        if answer == 'да':
            break
        elif answer == 'нет':
            break
        else:
            print(complain)
            retry -= 1
        print('Осталось попыток:', retry)

ask_user()
ask_user('Удалить файл?', 'Так удалить или нет?')
ask_user('Записать файл?')