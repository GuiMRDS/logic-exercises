# [5, 3, 8, 4, 2]
# → [2, 3, 4, 5, 8]


def bubble_sort(arr):
    size = len(arr)

    for _ in range(size-1):
        print(arr)
        for index in range(size-1):
            if arr[index] > arr[index+1]:
                arr[index], arr[index+1] = arr[index+1], arr[index]



print(bubble_sort([5,4,3,2,1]))
print(bubble_sort([5, 3, 8, 4, 2]))
