# Entrada:
# [1, 1, 2, 2, 3, 4, 4]

# Saída:
# [1, 2, 3, 4]


def TwoPointer(arr):
    if not arr:
        return []

    left = 0

    for right in range(1, len(arr)):
        if arr[right] != arr[left]:
            left += 1
            arr[left] = arr[right]

    return arr[:left + 1]


print(TwoPointer([1, 1, 2, 2, 3, 4, 4]))