ip_address = '{0}.{1}.{2}.{3}'
count = 0
numbers = []

while count < 4:
    new_number = int(input('Введите число: '))
    if 0 <= new_number <= 255:
        numbers.append(new_number)
        count += 1

ip = ip_address.format(
    numbers[0],
    numbers[1],
    numbers[2],
    numbers[3]
)
print(ip)