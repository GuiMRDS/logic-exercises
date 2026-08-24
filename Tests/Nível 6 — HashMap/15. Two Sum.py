array = [2, 7, 11, 15]
target = 9

# Saída:
# [0, 1]


def Hash_Two_Sum(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        sum = nums[left] + nums[right]

        if sum == target:
            return [left, right]

        elif sum < target:
            left += 1

        else:
            right -= 1


print(Hash_Two_Sum(array, target))