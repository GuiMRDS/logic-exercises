nums = [0,3,2,4]
target = 6

# Resposta:
# [2,3]

def twoSum(nums, target):
    size = len(nums)

    for i in range(size):
        for j in range(i+1, size):
            if nums[i] + nums[j] == target:
                return [i, j]

    return None


print(twoSum(nums, target))