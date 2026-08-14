array = [1, 3, 5, 7, 9]
target = 6

# Saída:
# 7


def elemento_binaria(array, target):
    esquerda = 0
    direita = len(array) - 1

    while esquerda != direita:
        if array[esquerda] >= target:
            return array[esquerda]

        esquerda += 1

    return -1


print(elemento_binaria(array, target))