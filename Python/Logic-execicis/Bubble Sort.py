def bubble(nums):
    size = len(nums)

    for i in range(size - 1):
        is_sorted = True

        print(nums)

        for j in range(size - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                is_sorted = False

        if is_sorted:
            return nums

    return nums


print(bubble([1, 4, 2, 3, 6, 5]))