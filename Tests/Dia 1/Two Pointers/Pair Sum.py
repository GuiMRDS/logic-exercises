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

        elif sum < target:
            left += 1

        else:
            right -= 1


    return False


print(pairSum(nums, target))