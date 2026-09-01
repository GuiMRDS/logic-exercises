# [1,2,3,1]

# true

def containsDuplicate(nums):
    visited = set()

    for num in nums:
        if num in visited:
            return True

        visited.add(num)

    return False


print(containsDuplicate([1,2,3,1]))
print(containsDuplicate([1,2,3,4,5]))