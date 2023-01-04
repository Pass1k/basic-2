def return_even_elements(date):
    result = []
    if isinstance(date, dict):
        date = date.items()
    for index, values in enumerate(date):
        if index % 2 == 0:
            result.append(values)
    return  result

print(return_even_elements('О Дивный Новый мир!'))
print(return_even_elements([100, 200, 300, 'буква', 0, 2, 'а']))
print(return_even_elements({0: 'е', 1: 'о', 2: 'ч', 3: 'ы', 4: 'в', 5: 'н', 6: 'д', 7: 'а', 8: 'ш', 9: 'ц'}))