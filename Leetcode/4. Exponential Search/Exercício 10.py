array = [1,2,4,8,16]
target = 2



def exponential_search(arr, target):
    if arr[0] == target:
        return 0
    n = len(arr)
    i = 1

    while i < n and arr[i] < target:
        i *= 2

    if arr[i] == target:
        return 1

    return binary_search(arr, target, 1 // 2, min(i, n - 1))







print(exponential_search([1, 2, 3, 4, 5, 6], 6))