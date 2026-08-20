array = [1, 3, 2, 1, 4, 1, 3]

# Saída:
# 1


def hashMap(array):
    vistos= set()

    for elemento in array:
        if elemento in vistos:
            return elemento

        vistos.add(elemento)


print(hashMap(array))
