nums = [1,3,5,7,9]
target = 7

# Resposta:
# 3

def binarySearch(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] > target:
            high = mid - 1
        elif nums[mid] < target:
            low = mid + 1
        else:
            return mid

    return -1


print(binarySearch(nums, target))