# [3,0,1]

# Resposta:
# 2

def HashSet(nums):
    visto = set()

    for num in nums:
        if num in visto:
            return num

        visto.add(num)

    return -1


print(HashSet([3,0,1]))