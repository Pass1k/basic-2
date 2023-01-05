players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}

rusult = []
for kay, values in players.items():
    v = list(values)
    k = list(kay)
    for i in v:
        k.append(i)
    rusult.append(tuple(k))

print(rusult)