# Entrada:
# [1, 1, 2, 2, 3, 4, 4]

# Saída:
# [1, 2, 3, 4]

array = [1, 1, 2, 2, 3, 4, 4]

def RemoverDuplicados(array):
    if not array:
        return 0

    esquerda = 0
    for direta in range(1, len(array)):
        if array[direta] != array[esquerda]:
            esquerda += 1
            array[esquerda] = array[direta]

    return esquerda + 1

quantidade = RemoverDuplicados(array)
print(array[:quantidade])