file = open('zen.txt', 'r')

lines = 0
words = 0
symbols = 0

for line in file:
    lines += 1
    words += len(line.split())
    symbols += len(line.strip('\n'))

print("Lines:", lines)
print("Words:", words)
print("Symbols:", symbols)