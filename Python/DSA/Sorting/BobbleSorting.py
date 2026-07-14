def bubble_sort(list):
    size = len(list)
    for i in range(size):
        print(list)
        for j in range(size-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]


bubble_sort([2,4,5,3,1])