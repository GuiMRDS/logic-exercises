# [1,2,3,1]

# true

def HashSetDuplicados(arr):
    visited = set()

    for num in arr:
        if num in visited:
            return True

        visited.add(num)

    return False


print(HashSetDuplicados([1,2,3,4,5]))
print(HashSetDuplicados([1,2,3,1]))