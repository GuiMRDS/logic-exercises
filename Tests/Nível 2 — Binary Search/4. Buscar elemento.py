array = [1, 3, 5, 7, 9, 11]
target = 7

# Saída:
# 3

def BinarySearch(array, target):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2

        if array[mid] == target:
            return mid

        elif array[mid] > target:
            right = mid - 1

        else:
            left = mid + 1


print(BinarySearch(array, target))