def binary_seacrh(nums, n):
    lo = 0
    hi = len(nums) - 1
    steps = 0

    while lo < hi:
        steps += 1
        mid = int((lo + hi) / 2)

        if nums[mid] == n:
            print("step: ", steps)
            return mid
        elif nums[mid] > n:
            lo = mid + 1
        else:
            hi = mid
    return -1

a = [1,2,3,4,5]
b = [1,2,3,4,5,6,7,8,9,10]

binary_seacrh(a, 3)