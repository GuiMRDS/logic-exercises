# [1,2,3,1]

# true


def HashSet(nums):
    visto = set()

    for num in nums:
        if num in visto:
            return True

        visto.add(num)

    return False


print(HashSet([1,2,3,1]))