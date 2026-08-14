array = [1, 3, 5, 6]
target = 4

# Saída:
# 2


def binary_search(array, target):
        esquerda = 0
        direita = len(array) - 1

        while esquerda <= direita:
            meio = (esquerda + direita) // 2

            if array[meio] == target:
                return meio

            elif array[meio] < target:
                esquerda = meio + 1

            else:
                direita = meio - 1

        return esquerda


print(binary_search(array, target))