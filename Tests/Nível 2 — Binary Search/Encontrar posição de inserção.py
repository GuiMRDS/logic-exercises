array = [1, 3, 5, 6]
target = 4

# Saída:
# 2

def binary_search(array, target):
    low = 0
    high = len(array) - 1

    while low <= high:
        if array[low] <= target and array[high] >= target:
            return array[low] + 1

        low += 1

    return -1


print(binary_search(array, target))