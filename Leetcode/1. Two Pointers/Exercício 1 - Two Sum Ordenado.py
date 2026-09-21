nums = [0,3,2,4]
target = 6

# Resposta:
# [2,3]

def TwoPointerBrute(nums, target):
    for i in range(len(nums) - 1):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]

    return False



print(TwoPointerBrute(nums, target))