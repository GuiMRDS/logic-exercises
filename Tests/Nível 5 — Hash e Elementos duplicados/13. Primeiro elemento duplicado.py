array = [2, 1, 3, 5, 3, 2]

# Saída:
# 3

def hash(array):
    vistos = set()

    for elemento in array:
        if elemento in vistos:
            return elemento

        vistos.add(elemento)


print(hash(array))
