array = [1, 3, 5, 6]
target = 4

# Saída:
# 2


def binary_search(array, target):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2

        if array[mid] == target:
            return mid

        elif array[mid] < target:
            left = mid + 1

        else:
            right = mid - 1


    return left


print(binary_search(array, target))




