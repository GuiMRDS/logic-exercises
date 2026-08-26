nums = [1,3,5,7,9]
target = 7

# Resposta:
# 3


def BinarySearch(nums, target):
    left = 0
    right = len(nums)-1

    while left <= right:
        mid = (left+right)//2

        if nums[mid] == target:
            return mid

        elif nums[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1


print(BinarySearch(nums, target))