nums = [3,2,4]
target = 6

# Resposta:
# [2,3]

def TwoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [nums[i], nums[j]]




print(TwoSum([1,2,3,4,5,6,7,8,9], 9))
print(TwoSum(nums, target))