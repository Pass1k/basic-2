
def findDisappearedNumbers(nums):
    numsout = []
    for i in range(1, len(nums) + 1):
        print(i)
        if i in nums:
            continue
        numsout.append(i)

    return numsout

num = [1, 1]
findDisappearedNumbers(num)
