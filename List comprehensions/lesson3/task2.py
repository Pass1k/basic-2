nums = [48, -10, 9, 38, 17, 50, -5, 43, 46, 12]

print('Первые пять элементов списка:', nums[:5])
print('Весь список, кроме последних двух элементов:', nums[:-2])
print('Все элементы с чётными индексами:', nums[::2])
print('Все элементы с нечётными индексами:', nums[1::2])
print('Все элементы в обратном порядке:', nums[::-1])
print('Все элементы списка через один в обратном порядке, начиная с последнего:', nums[::-2])