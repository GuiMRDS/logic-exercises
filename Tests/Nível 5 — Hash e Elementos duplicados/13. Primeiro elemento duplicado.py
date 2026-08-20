array = [2, 1, 3, 5, 3, 2]

# Saída:
# 3

def hash(array):
    vistos = set()

    for x in array:
        if x in vistos:
            return x

        vistos.add(x)

    return False


print(hash(array))
