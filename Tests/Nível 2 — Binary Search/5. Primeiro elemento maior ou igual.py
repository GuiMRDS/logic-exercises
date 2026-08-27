array = [1, 3, 5, 7, 9]
target = 6

# Saída:
# 7

def binary_search(array, target):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2

        if array[mid] >= target:
            return array[mid]

        else:
            low = mid + 1

    return -1


print(binary_search(array, target))