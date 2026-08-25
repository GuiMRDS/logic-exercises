# [3,0,1]

# Resposta:
# 2

def HashSet(nums):
    seen = set()

    for num in nums:
        if num not in seen:
            seen.add(num)

        return num

    return -1


print(HashSet([3,0,1]))