def quicksort(arr):
    if len(arr)<=1:
        return arr

    pivot = arr[0]

    less = [x for x in arr[1:] if x<=pivot]
    bigger = [x for x in arr[1:] if x>pivot]

    return quicksort(less) + [pivot] + quicksort(bigger)


arr = [9, 0, 2, 4, 1, 6, 7, 8]
arr = quicksort(arr)
print(arr)