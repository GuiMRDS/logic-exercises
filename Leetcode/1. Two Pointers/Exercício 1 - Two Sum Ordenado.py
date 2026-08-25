nums = [1,2,4,6,10]
target = 8

# Resposta:
# [2,3]


def TwoSum(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        sum = nums[left] + nums[right]

        if sum == target:
            return [left + 1, right]

        elif sum > target:
            right -= 1

        else:
            left += 1

    return -1


print(TwoSum(nums, target))