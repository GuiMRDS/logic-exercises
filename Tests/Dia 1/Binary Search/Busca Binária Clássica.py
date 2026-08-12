nums = [1,3,5,7,9,11]
target = 7

# saída
3

def BinarySearch(nums, target):
    low = 0
    high = len(nums)

    while low <= high:
        mid = (low+high)//2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid
    return -1

print(BinarySearch(nums, target))