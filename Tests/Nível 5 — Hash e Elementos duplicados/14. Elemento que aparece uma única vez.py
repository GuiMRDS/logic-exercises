array = [4, 1, 2, 1, 2]

# Saída:
# 4


def hash(array):
    visto = set()

    for num in array:
        if not num in visto:
            return num
        visto.add(num)

    return -1


print(hash(array))