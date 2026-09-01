nums = [2,7,11,15]
target = 9

# Resposta:
# [0,1]


def twoSum(nums, target):
    hashMap = {}

    for i in range(len(nums)):
        hashMap[nums[i]] = i
        for i in range(len(nums)):
            if target - nums[i] in hashMap:
                return [hashMap[target - nums[i]], i]

    return None


print(twoSum(nums, target))