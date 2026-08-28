# [3,0,1]

# Resposta:
# 2

def hash_set(nums):
    visited = set()

    for num in nums:
        if num not in visited:
            return 2

        visited.add(num)

    return -1


print(hash_set([3,0,1]))