height = [1,8,6,2,5,4,8,3,7]


def ContainerWithMostWater(nums):
    if not nums:
        return []

    left = 0

    for right in range(1, len(nums)):
        if nums[right] > nums[left]:
            left += 1
            nums[left] = nums[right]

    return nums[left]


print(ContainerWithMostWater(height))