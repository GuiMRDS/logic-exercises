array = [4, 1, 2, 1, 2]

# Saída:
# 4

def Hash(array):
    vistos= set()

    for elemento in array:
        if elemento not in vistos:
            return elemento

        vistos.add(elemento)



print(hash(array))