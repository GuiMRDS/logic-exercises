# [1,2,3,1]

# true


def hashSet(nums):
    visted = set()

    for num in nums:
        if num in visted:
            return True

        visted.add(num)

    return False


print(hashSet([1,2,3,1]))