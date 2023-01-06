string = input('Введите строку из 4 чисел: ')
tuple1 = (10, 20, 30, 40)
print('Кортеж чисел:', tuple1)
fa = zip(string, tuple1)

print(fa)

for i in fa:
    print(i)