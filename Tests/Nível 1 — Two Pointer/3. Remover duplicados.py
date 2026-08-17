# Entrada:
# [1, 1, 2, 2, 3, 4, 4]

# Saída:
# [1, 2, 3, 4]

entrada = [1, 1, 2, 2, 3, 4, 4]

def RemoverDuplicados(entrada):
    if not entrada:
        return False

    left = 0

    for right in range(len(entrada)-1):
        if entrada[right] != entrada[left]:
            left += 1
            entrada[left] = entrada[right]

    return left + 1


quantidade = RemoverDuplicados(entrada)
print(entrada[:quantidade])