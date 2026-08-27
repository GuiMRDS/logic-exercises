# [4, 1, 2, 1, 2]

# Saída:
# 4

def Hash(array):
    visto = set()

    for elemento in array:
        if elemento not in visto:
            return elemento

        visto.add(elemento)

    return False


print(Hash([4, 1, 2, 1, 2]))