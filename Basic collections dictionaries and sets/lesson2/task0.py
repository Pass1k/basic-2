def histogram(string):
    sym_dict = dict()
    for sym in string:
        if sym in sym_dict:
            sym_dict[sym] += 1
        else:
            sym_dict[sym] = 1
    return sym_dict

text = input('Введите текс: ').lower()
hist = histogram(text)

for i in sorted(hist.keys()):
    print(i, ':', hist[i])

print('Максимальная чистота: ', max(hist.values()))