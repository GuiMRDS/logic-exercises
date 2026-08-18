array = [-10, -5, -2, -1, 0, 3, 7, 10, 20]

def exponential_search(array, target):
    n = len(array)
    i = 0

    while i < n and array[i] < target:
        i *= 2

    if array[i] == target:
        return i

    return binary_search(array, i//2, min(i,n-1))


def binary_search(array, low, high):
    if high is None:
        high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2

        if mid > 0:
            return mid

        elif low < high:
            high = mid - 1

        else:
            low = mid + 1

    return -1