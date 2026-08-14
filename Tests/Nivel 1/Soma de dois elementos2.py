array = [1, 2, 4, 6, 8, 9, 14]
target = 10

# Saída:
# [2, 8]


def SomaElementos(array, target):
    left = 0
    right = len(array) - 1

    while left < right:
        sum = array[left] + array[right]

        if sum == target:
            return array[left], array[right]

        elif sum > target:
            right -= 1

        else:
            left += 1

    return False


print(SomaElementos(array, target))