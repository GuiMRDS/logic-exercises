array = [2, 3, 4, 10, 40, 50, 80, 100, 120]
target = 80

# Saída:
# 6


def binary_search(array, target, low=0, high=None):
    if high is None:
        high = len(array)-1

    while low <= high:
        mid = (low+high)//2

        if array[mid] == target:
            return mid

        elif array[mid] > target:
            high = mid - 1

        else:
            low = mid + 1

    return -1


def exponential_search(array, target):
    if array[0] == target:
        return 0

    n = len(array)
    i = 1

    while i < n and array[i] < target:
        i *= 2

    if array[i] == target:
        return i

    return binary_search(array, target, i//2, min(i,n-1))


print(exponential_search(array, target))