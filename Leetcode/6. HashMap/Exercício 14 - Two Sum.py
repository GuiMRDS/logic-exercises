nums = [2,7,11,15]

target = 9

# Resposta:
# [0,1]


def containsDuplicate(nums):
    left, right = 0, len(nums)-1

    while left < right:
        sum = nums[left] + nums[right]

        if sum == target:
            return True

        elif sum < target:
            left += 1

        else:
            right -= 1

    return False


print(containsDuplicate(nums))