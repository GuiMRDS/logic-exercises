nums = [1,3,5,7,9]
target = 7

# Resposta:
# 3


def BinarySearch(nums, target):
    low = 0
    high = len(nums)-1

    while low <= high:
        mid = (low+high)//2

        if nums[mid] >= target:
            return mid

        else:
            low = mid + 1

    return -1


print(BinarySearch(nums, target))