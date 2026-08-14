array = [1, 3, 5, 7, 9]
target = 6

# Saída:
# 7


def elemento_binaria(array, target):
    esquerda = 0
    direita = len(array) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2

        if array[meio] > target:
            return array[meio]

        elif array[meio] < target:
            esquerda = meio + 1

        else:
            direita = meio + 1


print(elemento_binaria(array, target))