array = [2, 3, 4, 10, 40, 50, 80, 100, 120]
target = 80

# Saída:
# 6

def exponential_search(array, target):
    low = 0
    high = len(array) - 1

    while low <= high:
        low *= 2

    if low == target:
        return low

    return binary_seacrh()