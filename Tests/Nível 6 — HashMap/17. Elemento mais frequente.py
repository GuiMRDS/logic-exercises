array = [1, 3, 2, 1, 4, 1, 3]

# Saída:
# 1


def HashMap(array):
    hashMap = set()

    for elemento in array:
        if elemento in hashMap:
            return elemento

        hashMap.add(elemento)

    return None


print(HashMap(array))

