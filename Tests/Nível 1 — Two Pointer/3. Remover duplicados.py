# Entrada:
# [1, 1, 2, 2, 3, 4, 4]

# Saída:
# [1, 2, 3, 4]


def TwoPointer(array):
    left = 0
    right = len(array)-1

    while left < right:
        if array[left] == array[right]:
            array[left], array[right] = array[right], array[left]

        left += 1
        right -= 1

    return False


print(TwoPointer([1, 1, 2, 2, 3, 4, 4]))