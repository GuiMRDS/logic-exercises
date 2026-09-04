nums = [0,3,2,4]
target = 6

# Resposta:
# [2,3]

def TwoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

    return None


print(TwoSum(nums, target))