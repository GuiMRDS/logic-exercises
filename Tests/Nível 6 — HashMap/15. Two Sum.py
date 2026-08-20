array = [2, 7, 11, 15]
target = 9

# Saída:
# [0, 1]


def twoSum(array, target):
    left = 0
    right = len(array) - 1

    while left <= right:
        soma = array[left] + array[right]

        if soma == target:
            return [left, right]

        elif soma < target:
            left += 1

        else:
            right -= 1

    return None



print(twoSum(array, target))