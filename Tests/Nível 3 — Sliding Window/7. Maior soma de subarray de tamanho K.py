array = [2, 1, 5, 1, 3, 2]
k = 3

# Saída:
# 9


def SomaMaxima(array, k):
    soma = sum(array[:k])
    maior = soma

    for direita in range(k, len(array)):
        soma = soma - array[direita - k] + array[direita]
        maior = max(maior, soma)

    return maior


print(SomaMaxima(array, k))