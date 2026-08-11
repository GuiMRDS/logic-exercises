nums = [1,3,5,7,9,11]
target = 7

# saída
3

def binary_search(nums, target):
    lo = 0
    hi = len(nums)
    steps = 0

    while lo < hi:
        steps += 1
        mid = int((lo + hi) / 2)

        if nums(mid) == target:
            print("step: ", steps)
            return mid
        elif nums(mid) < target:
            lo = mid + 1
        else:
            hi = mid
    return -1



binary_search(nums, target)