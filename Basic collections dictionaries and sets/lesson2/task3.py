def program(string):
    symbols = dict()
    for sym in string:
        if sym in symbols:
            symbols[sym] += 1
        else:
            symbols[sym] = 1
    return symbols

text = input('Введите текст: ')
hist = program(text)

for i in sorted(hist.keys()):
    print(i, '-', hist[i])

print('Максимальная чистота: ', max(hist.values()))
