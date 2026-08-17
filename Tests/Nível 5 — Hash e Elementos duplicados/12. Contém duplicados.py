# [1, 2, 3, 4]
# → false

# [1, 2, 3, 1]
# → true

array = [1, 2, 3, 4]
array2 = [1, 2, 3, 1]

def Hash(array):
    visto = set()

    for n in array:
        if n in visto:
            return True
        visto.add(n)

    return False


print(Hash(array))
print(Hash(array2))