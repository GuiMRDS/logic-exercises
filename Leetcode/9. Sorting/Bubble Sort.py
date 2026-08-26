def bubbleSort(arr):
    tamanho = len(arr)

    for _ in range(tamanho-1):
        for i in range(tamanho-1):
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
                print(arr)

    return arr


print(bubbleSort([4,5,2,1,3]))