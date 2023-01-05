familys = {
    'Сидоров':{
        'Сидоров Никита': 35,
        'Сидорова Алина': 34,
        'Сидоров Павел': 10
    }
}

surname = input('Введите фамилию: ')

if surname in familys:
    for i in familys[surname]:
        print(i)
else:
    print('Такой семьи нету')