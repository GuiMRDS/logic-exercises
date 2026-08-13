nums = [1,1,2,2,3,4,4]

# Saída:
# [1,2,3,4]

def remove_duplicates(nums):
    if not nums:
        return 0

    left = 0

    for right in range(len(nums)):
        if nums[right] != nums[left]:
            left += 1
            nums[left] = nums[right]

    return nums[:left + 1]


print(remove_duplicates(nums))