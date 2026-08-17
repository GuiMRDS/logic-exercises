array = [1, 3, 5, 7, 9, 11]
target = 7

# Saída:
# 3

def buscar(entrada, target):
    left = 0
    right = len(entrada) - 1

    while left <= right:
        mid = (left + right) // 2

        if entrada[mid] == target:
            return mid

        elif entrada[mid] > target:
            right = mid - 1

        else:
            left = mid + 1


print(buscar(array, target))