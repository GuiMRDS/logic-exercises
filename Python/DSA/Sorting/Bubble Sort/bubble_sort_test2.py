def bubble_sort(arr):
    size = len(arr)
    for i in range(size):
        is_sorted = True
        print(arr)
        for j in range(size-1):
            if arr[j] > arr[j+1]:
                is_sorted = False
                arr[j],arr[j+1] = arr[j+1],arr[j]
        if is_sorted:
            break



bubble_sort([3,5,1,2,4])