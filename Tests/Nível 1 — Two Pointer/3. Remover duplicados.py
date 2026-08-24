# Entrada:
# [1, 1, 2, 2, 3, 4, 4]

# Saída:
# [1, 2, 3, 4]


def TwoPointer(array):
    visto = set()

    for num in array:
        if num in visto:
            visto.remove(num)

        visto.add(num)

    return visto


print(TwoPointer([1, 1, 2, 2, 3, 4, 4]))