nums = [2,7,11,15]
target = 9

# Resposta:
# [0,1]


def twoSumHash(nums, target):
    hashMap = {}

    for i in range(len(nums)):
        hashMap[nums[i]] = i

        for j in range(len(nums)):
            if nums[j] in hashMap:
                return hashMap[nums[j]]

    return False


print(twoSumHash(nums, target))