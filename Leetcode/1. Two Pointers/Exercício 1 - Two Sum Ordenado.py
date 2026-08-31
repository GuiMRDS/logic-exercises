nums = [3,2,4]
target = 6

# Resposta:
# [2,3]

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return [nums[i],nums[j]]



print(twoSum(nums,target))