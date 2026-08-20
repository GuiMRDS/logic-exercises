array = [1, 2, 2, 3, 1, 1]

# Saída:
# 1 → 3
# 2 → 2
# 3 → 1


def hashMap(array):
    hashMap = set()

    for elemento in array:
        hashMap.add(elemento)

    return hashMap



print(hashMap(array))