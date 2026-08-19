# [5, 3, 8, 4, 2]
# → [2, 3, 4, 5, 8]


def bubble_sort(array):
    size = len(array)

    for _ in array:
        print(array)
        for i in range(size - 1):
            if array[i] > array[i + 1]:
                array[i+1], array[i] = array[i], array[i+1]



bubble_sort([5, 3, 8, 4, 2])