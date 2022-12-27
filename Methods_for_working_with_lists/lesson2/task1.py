main = [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1]

first_company = [0, 0, 0]

second_company = [1, 0, 0, 1, 1]

third_company = [1, 1, 1, 0, 1]

all = [first_company, second_company, third_company]

for i in all:
    main.extend(i)

not_solved = main.count(0)


print(f'Результат работы программы: \nОбщий список задач: {main}\nКол-во невыполненных задач: {not_solved}')