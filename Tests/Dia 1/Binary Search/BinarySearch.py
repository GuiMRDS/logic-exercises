a = [1,2,3,4,5]
b = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
c = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
d = [1,2,3,4,5,6,7,8,9,10,]

def binary_search(nums, target):
    low = 0
    high = len(nums)
    steps = 0

    while low < high:
        mid = (low + high) // 2
        steps += 1

        if nums[mid] == target:
            print("steps: ", steps)
            return mid

        elif nums[mid] < target:
            low = mid + 1

        elif nums[mid] > target:
            high = mid

    return -1

print(binary_search(a,3))
print(binary_search(b,3))
print(binary_search(c,3))
print(binary_search(d,3))