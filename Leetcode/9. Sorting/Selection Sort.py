def selection_sort(arr):
    n = len(arr)

    for i in range(len(arr)):
        min_idx = i

        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


def selection_sort_2(arr):
    n = len(arr)

    for i in range(n):
        min_idx = i

        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

print(selection_sort([5,4,3,2,1]))
print(selection_sort_2([5,4,3,2,1]))