array = [1, 3, 5, 7, 9, 11]
target = 7

# Saída:
# 3


def BinarySearch(array, target):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2

        if array[mid] == target:
            return mid

        elif array[mid] > target:
            high = mid - 1

        else:
            low = mid + 1

    return -1


print(BinarySearch(array, target))