nums = [1, 2, 2, 3, 4, 4, 5]

# [1, 2, 3, 4, 5]

def RemoverDuplicados(nums):
    for num in nums:
        if nums.count(num) > 1:
            nums.remove(num)
        print(num)


RemoverDuplicados(nums)