array = [2, 1, 3, 5, 3, 2]

# Saída:
# 3


def Hash(array):
    visto = set()
    contador = set()

    for n in array:
        contador.add(n)
        if n in visto:
            if contador == visto:
                return n

        visto.add(n)

    return False

print(Hash(array))