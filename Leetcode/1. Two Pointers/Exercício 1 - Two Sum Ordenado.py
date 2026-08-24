nums = [1,2,4,6,10]
target = 8

# Resposta:
# [2,3]


def TwoSum(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        soma = nums[left] + nums[right]

        if soma == target:
            return nums[left], right

        elif soma < target:
            left += 1

        else:
            right -= 1

    return None


print(TwoSum(nums, target))