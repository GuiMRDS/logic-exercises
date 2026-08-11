nums = [1,1,2,2,3,4,4]

[1,2,3,4]


def RemoverDuplicados(nums):
    for num in nums:
        if nums.count(num) > 1:
            nums.remove(num)
        print(nums)


RemoverDuplicados(nums)