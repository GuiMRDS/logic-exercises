# Entrada:
# [1, 1, 2, 2, 3, 4, 4]

# Saída:
# [1, 2, 3, 4]


def TwoPointer(arr):
    if not arr:
        return 0

    left = 0
    for right in range(len(arr)):
        if arr[right] != arr[left]:
            left += 1
            arr[left] =  arr[left]

    return left + 1


array = [1, 1, 2, 2, 3, 4, 4]
quantidade = TwoPointer(array)
print(array[:quantidade])