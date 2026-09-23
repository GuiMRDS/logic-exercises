nums = [0,3,2,4]
target = 6

# Resposta:
# [2,3]




def TwoPointer(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        sum = nums[left] + nums[right]

        if sum == target:
            return nums[left], nums[right]

        if sum < target:
            left = left + 1

        else:
            right = right - 1

    return False


print(TwoPointerBruteForce(nums, target))
print(TwoPointer([1, 2, 4, 6, 10], 8))