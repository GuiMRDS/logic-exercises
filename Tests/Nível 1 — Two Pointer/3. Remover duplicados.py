# Entrada:
# [1, 1, 2, 2, 3, 4, 4]

# Saída:
# [1, 2, 3, 4]


def TwoPointer(arr):
    left = 0
    right = 1
    size = len(arr)

    while right < size:
        if arr[left] == arr[right]:
            arr[left] = arr[right]
            left += 1
            right += 1

        left += 1
        right += 1

    return arr



print(TwoPointer([1, 1, 2, 2, 3, 4, 4]))