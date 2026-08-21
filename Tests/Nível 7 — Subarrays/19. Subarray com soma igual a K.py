array = [1, 1, 1]
k = 2

# Saída:
# 2

def MaiorSubarrays(array, k):
    soma = sum(array[:k])
    maior = soma

    for direita in range(k, len(array)):
        soma = soma - array[direita - k] + array[direita]
        maior = max(soma, maior)

    return maior


print(MaiorSubarrays(array, k))