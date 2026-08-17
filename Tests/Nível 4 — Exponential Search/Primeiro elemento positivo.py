entrada = [-10, -5, -2, -1, 0, 3, 7, 10, 20]
negativo = 0

def binary_search(array, target, low=0, high=None):
    if high is None:
        high = len(array)-1

    while low <= high:
        mid = (low+high)//2

        if array[mid] == target:
            return array[mid]

        elif array[mid] > target:
            high = mid - 1

        else:
            low = mid + 1

    return -1


def exponential_search(array):
    if array[0] == negativo:
        return 0

    n = len(array)
    i = 1

    while i <= n and array[i] == negativo:
        i *= 2

    if array[i] > negativo - 1:
        return i


    return binary_search(array, negativo - i//2, min(i,n-1))


print(exponential_search(entrada))