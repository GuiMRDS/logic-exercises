# [1, 2, 3, 4]
# → false

# [1, 2, 3, 1]
# → true


def hash(array):
    vistos = set()

    for num in array:
        if num in vistos:
            return True

        vistos.add(num)

    return False



print(hash([1, 2, 3, 4]))
print(hash([1, 2, 3, 1]))