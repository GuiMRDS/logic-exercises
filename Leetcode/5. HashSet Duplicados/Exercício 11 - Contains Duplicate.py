# [1,2,3,1]

# true

def HashSet(array):
    vistos = set()

    for i in array:
        if i in vistos:
            return True

        vistos.add(i)

    return False


print(HashSet([1,2,3,1]))