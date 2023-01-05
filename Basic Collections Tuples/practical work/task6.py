the_list = [i for i in range(10)]
print([*map(tuple, zip(the_list[::2], the_list[1::2]))])
