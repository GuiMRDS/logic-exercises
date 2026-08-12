nums = [1,2,4,4,4,7,9]
target = 4

# saída
# 2

def PrimeiroElementoMaior(nums, target):
    left = 0
    right = len(nums)
    steps = 0

    while left <= right:
        mid = (left + right) // 2
        steps += 1

        if nums[mid] == target:
            print("steps: ", steps)
            return mid
        elif nums[mid] < target:
            right = mid + 1
        else:
            left = mid

    return -1


print(PrimeiroElementoMaior(nums, target))