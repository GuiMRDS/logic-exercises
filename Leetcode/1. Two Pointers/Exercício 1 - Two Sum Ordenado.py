nums = [3,2,4]
target = 6

# Resposta:
# [2,3]


def TwoPointer(nums):
    n = len(nums)

    for i in range(n):
        for j in range(n):
            if nums[i] + nums[j] == target:
                return [nums[i], nums[j]]

    return None


print(TwoPointer(nums))