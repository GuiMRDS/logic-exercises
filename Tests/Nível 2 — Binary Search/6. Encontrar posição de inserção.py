array = [1, 3, 5, 6]
target = 4

# Saída:
# 2

def binary_search(array, target):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2

        if array[mid] >= target:
            return mid

        else:
            low = mid + 1

    return -1


print(binary_search(array, target))