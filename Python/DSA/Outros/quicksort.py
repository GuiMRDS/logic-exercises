def quicksort(arr, left, right):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        bigger_than_pivot = [x for x in arr[1:] if x > pivot]
        return quicksort(less_than_pivot) + [pivot] + quicksort(bigger_than_pivot)

arr = [0, 2, 2, 4, 7,8,9]

arr = quicksort(arr)

print(arr)