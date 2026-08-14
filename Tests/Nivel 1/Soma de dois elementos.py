array = [1, 2, 4, 6, 8, 9, 14]
target = 10

# Saída:
# [2, 8]


def SomaElementos(array, target):
    esquerda = 0
    direita = len(array) - 1

    while esquerda < direita:
        soma = array[esquerda] + array[direita]

        if soma == target:
            return array[esquerda], array[direita]

        elif soma < target:
            esquerda += 1

        else:
            direita -= 1

    return False


print(SomaElementos(array, target))