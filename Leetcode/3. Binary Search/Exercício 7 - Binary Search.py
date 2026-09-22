nums = [1,3,5,7,9]
target = 7

# Resposta:
# 3


def BinarySearch(nums, target):
    left = 0
    right = len(nums)-1

    while(left < right):
        mid = (left + right) // 2

        if mid == target:
            return mid

        elif mid < target:
            mid = mid - 1

        else:
            mid = mid + 1

    return False



print(BinarySearch(nums, target))