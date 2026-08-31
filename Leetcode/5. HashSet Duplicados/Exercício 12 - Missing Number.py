# [3,0,1]

# Resposta:
# 2

def hashSet(nums):
    visted = set()

    for num in nums:
        if num in visted:
            return visted

        visted.add(num)

    return len(visted)


print(hashSet([3,0,1]))