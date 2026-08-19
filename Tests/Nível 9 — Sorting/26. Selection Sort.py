# [64, 25, 12, 22, 11]
# → [11, 12, 22, 25, 64]


def selection_sort(array):
    size = len(array)

    for _ in array:
        print(array)
        for i in range(size - 1):
            if array[i] > array[i + 1]:
                array[i + 1], array[i] = array[i], array[i + 1]


selection_sort([64, 25, 12, 22, 11])