lst_data = []
start = 1
end = 10

for i in range(4):
    lst_data.append([x for x in range(start, end, 4)])
    start += 1
    end += 1

print(lst_data)
