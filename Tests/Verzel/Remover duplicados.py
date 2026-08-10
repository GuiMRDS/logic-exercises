nums = [1, 2, 2, 3, 4, 4, 5]

def removeDuplicates(nums):
    n = len(nums)

    for i in range(n):
        for j in range(n):
            if nums[i] != nums[j]:
                nums[i] = nums[j]
                print(j)

    return False

removeDuplicates(nums)