array = [1, 2, 2, 3, 1, 1]

# Saída:
# 1 → 3
# 2 → 2
# 3 → 1


def hashMap(array):
    vistos = set()

    for elemento in array:
        vistos.add(elemento)

    return vistos


print(hashMap(array))