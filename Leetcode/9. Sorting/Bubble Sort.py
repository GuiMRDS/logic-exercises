def bubble_sort(arr):
    size = len(arr)

    for i in range(size):
        for j in range(size - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


print(bubble_sort([2,3,4,5,6,7,8,9]))