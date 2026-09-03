nums = [2,7,11,15]
target = 9

# Resposta:
# [0,1]


def twoSumHashMap(nums, target):
    hashMap = {}

    for i in range(len(nums)):
        hashMap[nums[i]] = i
        for j in range(len(nums)):
            if target - nums[j] in hashMap:
                return [hashMap[target - nums[j]], j]
            else:
                hashMap[nums[j]] = i
    return None



print(twoSumHashMap(nums, target))