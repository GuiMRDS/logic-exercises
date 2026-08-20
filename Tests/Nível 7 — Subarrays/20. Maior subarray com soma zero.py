array = [15, -2, 2, -8, 1, 7, 10, 23]
k = 0

# Saída:
# 5

def SubarraySum(array, k):
    prefix_sum = 0
    maior = 0

    indices = {0: -1}

    for i, num in enumerate(array):
        prefix_sum += num

        if prefix_sum - k in indices:
            tamanho = i - indices[prefix_sum - k]
            maior = max(maior, tamanho)

        if prefix_sum not in indices:
            indices[prefix_sum] = i

    return maior


print(SubarraySum(array, 0))


print(SubarraySum(array, k))