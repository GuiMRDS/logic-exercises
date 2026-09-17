nums = [0,3,2,4]
target = 6

# Resposta:
# [2,3]

def TwoPointerBruteForce(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]

    return False


def TwoPointer(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        sum = nums[left] + nums[right]

        if sum == target:
            return nums[left], nums[right]

        if nums[left] > nums[right]:
            left = left + 1

        else:
            right = right - 1



print(TwoPointerBruteForce(nums, target))
print(TwoPointer(nums, target))