array = [1, 3, 5, 7, 9]
target = 6

# Saída:
# 7


def ElementorMaiorOuIgual(array, target):
    left = 0
    right = len(array)-1

    while left <= right:
        mid = (left+right)//2

        if array[mid] >= target:
            return mid
