array = [1, 2, 4, 6, 8, 9, 14]
target = 10

# Saída:
# [2, 8]


def soma(array, target):
    left = 0
    right = len(array) - 1

    while left < right:
        soma = array[left] + array[right]

        if soma == target:
            return array[left], array[right]

        elif soma < target:
            left += 1

        else:
            right -= 1

    return False


print(soma(array, target))