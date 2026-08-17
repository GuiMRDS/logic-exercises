# [4, 1, 2, 1, 2]

# Saída:
# 4


array = [4, 1, 2, 1, 2]


def hash(array):
    visto = set()

    for n in array:
        if not n in visto:
            return n

        visto.add(n)

    return False


print(hash(array))
