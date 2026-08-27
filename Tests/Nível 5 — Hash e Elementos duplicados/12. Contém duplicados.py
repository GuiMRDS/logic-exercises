# [1, 2, 3, 4]
# → false

# [1, 2, 3, 1]
# → true


def Hash(array):
    visto = set()

    for num in array:
        if num in visto:
            return True

        visto.add(num)

    return False


print(Hash([1, 2, 3, 4]))
print(Hash([1, 2, 3, 1]))