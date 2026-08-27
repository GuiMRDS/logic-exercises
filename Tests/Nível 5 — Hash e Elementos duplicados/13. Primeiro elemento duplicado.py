# [2, 1, 3, 5, 3, 2]

# Saída:
# 3

def Hash(array):
    visto = set()

    for elemento in array:
        if elemento not in visto:
            return array[elemento]

        visto.add(elemento)

    return None


print(Hash([2, 1, 3, 5, 3, 2]))