# [1, 2, 3, 4]
# → false

# [1, 2, 3, 1]
# → true

array = [1, 2, 3, 4]
array1 = [1, 2, 3, 1]

def Hash(array):
    visto = set()

    for num in array:
        if num in visto:
            return True
        visto.add(num)

    return False


print(Hash(array))
print(Hash(array1))