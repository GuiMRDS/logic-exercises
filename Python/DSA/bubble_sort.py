def bubble(nums):
    size = len(nums)

    for i in nums:
        is_sorted = True

        print(nums)
        for j in range(size-1):
            if nums[j] > nums [j+1]:
                is_sorted = False
                nums[j+1], nums[j] = nums[j], nums[j+1]
            if is_sorted:
                return



bubble([1,2,5,4,3])