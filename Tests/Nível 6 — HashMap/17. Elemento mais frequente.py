array = [1, 3, 2, 1, 4, 1, 3]

# Saída:
# 1


def hashMap(array):
    visited = set()

    for elemento in array:
        if elemento in visited:
            return elemento

        visited.add(elemento)

    return -1


print(hashMap(array))
