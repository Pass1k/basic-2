while True:
    password = input('Придумайте пароль: ')

    lenght = len(password)
    capital_letters = len([letter for letter in password if letter.isupper()])
    numbers = len([numbers for numbers in password if numbers.isdigit()])

    if (lenght > 8) and (capital_letters >= 1) and (numbers >= 3):
        print('Это надёжный пароль!')
        break
    print('Пароль ненадёжный. Попробуйте ещё раз.')
