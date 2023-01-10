families = {
    'Сидоров Никита':35,
    'Сидорова Алина':34,
    'Сидоров Павел':10,
    'Петров Виктор':15,
    'Петрова Дарья':16
}


search = input('Кого ищем? ').lower()
result = []
for _ in families:
    if search in _.split()[0].lower():
        result.append(_+' '+str(families[_]))
