def summ(*args):
    def flaten(a_list):
        result = []
        for e in a_list:
            if isinstance(e, int):
                result.append(e)
            else:
                result.extend(flaten(e))
        return result
    return sum(flaten(args))


print(summ([[1, 2, [3]], [1], 3]))
print(summ(1,2,3,4,5))
