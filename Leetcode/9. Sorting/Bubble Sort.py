def bubbleSort(nums):
    for i in range(len(nums)):
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

    return nums


print(bubbleSort([9,8,7,6,5,4,3,2,1]))