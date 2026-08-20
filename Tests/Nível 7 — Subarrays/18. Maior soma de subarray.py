array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

# Saída:
# 6

def MaiorSubarrays(array):
    atual = array[0]
    maior = array[0]

    for i in range(1, len(array)):
        atual = max(array[i], atual + array[i])
        maior = max(maior, atual)

    return maior


print(MaiorSubarrays(array))
