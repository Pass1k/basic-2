r = open('zen.txt', 'r')

text = [i for i in r]

for i in text[::-1]:
    print(i, end='')