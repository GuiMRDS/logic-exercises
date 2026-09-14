nums = [0,3,2,4]
target = 6

# Resposta:
# [2,3]

def TwoPointerBruteForce(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]

    return False


def TwoPointer(nums, target):
    left = 0
    right = len(nums)

    while left < right:
        if nums[left] + nums[right] == target:
            return [i,j]
        elif nums[left] < target:
            left = left + 1
        else:
            right = right - 1

    return False


print(TwoPointerBruteForce(nums, target))
print(TwoPointer(nums, target))