# [1,2,3,1]

# true

def HashSet(nums):
    visto = set()

    for i in nums:
        if i in visto:
            return True

        visto.add(i)

    return False


print(HashSet([1,2,3,1]))
print(HashSet([1,2,3,4]))