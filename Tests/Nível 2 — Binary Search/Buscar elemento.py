array = [1, 3, 5, 7, 9, 11]
target = 7

# Saída:
# 3

# Saída:
# -1

def buscar(array, target):
    esquerda = 0
    direta = len(array) - 1

    while esquerda < direta:
        if array[esquerda] == target:
            return array[esquerda]

        esquerda += 1

    return -1


print(buscar(array, target))