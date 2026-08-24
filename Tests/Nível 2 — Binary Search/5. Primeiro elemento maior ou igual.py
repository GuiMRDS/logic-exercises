array = [1, 3, 5, 7, 9]
target = 6

# Saída:
# 7


def BinarySearch(array, target):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2

        if array[mid] >= target:
            return array[mid]

        else:
            left = mid + 1



print(BinarySearch(array, target))