# [2, 1, 3, 5, 3, 2]

# Saída:
# 3

def Hash(array):
    visto = set()

    for num in array:
        if num in visto:
            return num

        visto.add(num)

    return -1


print(Hash([2, 1, 3, 5, 3, 2]))