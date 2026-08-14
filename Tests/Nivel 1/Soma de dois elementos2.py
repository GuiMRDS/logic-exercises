array = [1, 2, 4, 6, 8, 9, 14]
target = 10

# Saída:
# [2, 8]


def SomaElementos(array, target):
    if not array:
        return 0

    esquerda = 0
    for direita in range(0, len(array)):
        if array[direita] + array[esquerda] == target:
            return array[esquerda], array[direita]

        elif array[direita] + array[esquerda] < target:
            esquerda += 1

        else:
            direita -= 1

    return False


print(SomaElementos(array, target))