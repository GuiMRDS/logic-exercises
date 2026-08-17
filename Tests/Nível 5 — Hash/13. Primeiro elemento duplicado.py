array = [2, 1, 3, 5, 3, 2]

# Saída:
# 3


def HashMap(array):
    visto = set()

    for n in array:
        if n in visto:
            return n
        visto.add(n)

    return False


print(HashMap(array))