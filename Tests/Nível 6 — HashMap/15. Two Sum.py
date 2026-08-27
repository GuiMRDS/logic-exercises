array = [2, 7, 11, 15]
target = 9

# Saída:
# [0, 1]


def two_Sum_Hash(array, target):
    left = 0
    right = len(array) - 1

    while left < right:
        sum = array[left] + array[right]

        if sum == target:
            return [left, right]

        elif sum < target:
            left += 1

        else:
            right -= 1

    return False


print(two_Sum_Hash(array, target))