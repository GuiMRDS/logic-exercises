array = [4, 1, 2, 1, 2]

# Saída:
# 4


def Hash(array):
    visto = set()

    for n in array:
        if not n in visto:
            return n
        visto.add(n)

    return False


print(Hash(array))