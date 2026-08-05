def bubble_sort(nums):
    size = len(nums)
    for i in nums:
        is_sorted = True
        print(nums)
        for j in range(size-1):
            if nums[j] > nums[j+1]:
                is_sorted = False
                nums[j], nums[j+1] = nums[j+1], nums[j]
        if is_sorted:
            break



print("----------------")
bubble_sort([5,4,3,2,1])
print("----------------")
bubble_sort([1,2,3,4,5])
print("----------------")
bubble_sort([1,5,3,2,5])
print("----------------")