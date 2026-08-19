# [5, 3, 8, 4, 2]
# → [2, 3, 4, 5, 8]


def bubble_sort(arr):
    tamanho = len(arr)

    for _ in arr:
        print(arr)
        for i in range(tamanho-1):
            if arr[i] > arr[i+1]:
                arr[i + 1], arr[i] = arr[i], arr[i + 1]



print(bubble_sort([5,4,3,2,1]))
print(bubble_sort([5, 3, 8, 4, 2]))
