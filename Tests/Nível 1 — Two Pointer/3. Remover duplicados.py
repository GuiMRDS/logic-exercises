# Entrada:
# [1, 1, 2, 2, 3, 4, 4]

# Saída:
# [1, 2, 3, 4]


def TwoPointer(array):
    left = 0

    for right in range(len(array) - 1):
        if array[right] == array[left]:
            array[left] = array[right]
            left += 1

        left += 1


    return left + 1

array = [1, 1, 2, 2, 3, 4, 4]
print(TwoPointer(array))