def tpl_sort(string):
    status = True
    for i in string:
        if type(i) is int:
            continue
        else:
            status = False
            break

    if status:
        sort = sorted(string)
        sort = tuple(sort)
        print(sort)
    else:
        print(string)

tuple1 = (6, 3, -1, 8, 4, 10, -5)
tpl_sort(tuple1)
