# [1, 2, 3, 4]
# → false

# [1, 2, 3, 1]
# → true


def hash(array):
    visto = set()

    for num in array:
        if num in visto:
            return True

        visto.add(num)

    return False


print(hash([1, 2, 3, 4]))
print(hash([1, 2, 3, 1]))