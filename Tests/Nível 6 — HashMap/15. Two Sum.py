array = [2, 7, 11, 15]
target = 9

# Saída:
# [0, 1]


def twoSum(array, target):
    left = 0
    right = len(array) - 1

    while left < right:
        mid = (left + right) // 2

        if array[mid] == target:
            return [array[left], array[mid]]

        elif array[mid] > target:
            right = mid - 1

        else:
            left = mid + 1

    return False


print(twoSum(array, target))