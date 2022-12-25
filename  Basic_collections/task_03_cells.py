a_cells = int(input('Количество клеток: '))
res_cells = []

for i in range(a_cells):
    cell = int(input(f'Эффективность {i + 1} клетки: '))
    if cell < i + 1:
        res_cells.append(cell)

print(f'Неподходящие значения: {res_cells}')

