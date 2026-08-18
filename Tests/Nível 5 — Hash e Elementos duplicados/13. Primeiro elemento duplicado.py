array = [2, 1, 3, 5, 3, 2]

# Saída:
# 3

def hash(array):
    visto = set()

    for elemento in array:
        if elemento in visto:
            return elemento
        visto.add(elemento)

    return -1

print(hash(array))