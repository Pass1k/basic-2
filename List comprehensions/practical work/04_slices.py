alphabet = 'abcdefg'

copy = alphabet

print('Копию строки', copy)
print('Элементы строки в обратном порядке:', copy[::-1])
print('Каждый второй элемент строки (включая самый первый):', copy[::2])
print('Каждый второй элемент строки после первого', copy[1::2])
print('Все элементы до второго', copy[:1])
print('Все элементы начиная с конца до предпоследнего:', copy[-1:])
print('Все элементы в диапазоне индексов от 3 до 4 (не включая 4):', copy[3:4])
print('Последние три элемента строки:', copy[-3::])
print('Все элементы в диапазоне индексов от 3 до 4:', copy[3:5])
print('То же, что и в предыдущем пункте, но в обратном порядке:', copy[-3:-5:-1])
