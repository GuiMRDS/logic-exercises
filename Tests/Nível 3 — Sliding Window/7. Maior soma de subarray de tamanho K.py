array = [2, 1, 5, 1, 3, 2]
k = 3

# Saída:
# 9


def SomaMaxima(array, k):
    esquerda = 0
    direita = 0

    soma = 0
    maior = 0

    while direita < len(array):

        soma += array[direita]

        while direita - esquerda + 1 > k:
            soma -= array[esquerda]
            esquerda += 1

        if direita - esquerda + 1 == k:
            maior = max(maior, soma)

        direita += 1

    return maior

print(SomaMaxima(array, k))