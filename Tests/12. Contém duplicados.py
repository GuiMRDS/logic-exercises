# [1, 2, 3, 4]
# → false

# [1, 2, 3, 1]
# → true

array = [1, 2, 3, 4]
array2 = [1, 2, 3, 1]


def HashMap(nums):
    seen_numbers = set()

    for n in nums:
        if n in seen_numbers:
            return True
        seen_numbers.add(n)

    return False



print(HashMap(array))
print(HashMap(array2))
