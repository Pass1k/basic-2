def selection_sort(my_list):
    for i_min in range(len(my_list)):
        for current in range(i_min,len(my_list)):
            if my_list[current] < my_list[i_min]:
                my_list[current], my_list[i_min] = my_list[i_min], my_list[current]

nums = [4, 9, 7, 6, 3, 2]

selection_sort(nums)

print(nums)