nums = [1, 2, 4, 7, 11, 15]
target = 15

# saída
# (2, 4)

def pairSum(nums, target):
    left = 0
    right = len(nums)-1

    while left < right:
        sum = nums[left] + nums[right]

        if sum == target:
            return [left, right]

        if sum < target:
            left += 1

        if sum > target:
            right -= 1

    return None

print(pairSum(nums, target))