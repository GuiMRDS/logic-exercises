array = [2, 1, 5, 1, 3, 2]
k = 3

# Saída:
# 9

def SlidingWindow(array, k):
    soma = sum(array[:k])
    maior = soma

    for direta in range(k, len(array)):
        soma = soma - array[direta - k] + array[direta]
        maior = max(maior, soma)

    return maior


print(SlidingWindow(array, k))
