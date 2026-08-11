nums = [1, 2, 4, 7, 11, 15]
target = 15

# saída
(2, 4)

def pairSum(nums):
    n = len(nums)

    for i in range(n):
        for j in range(n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None


print(pairSum(nums))