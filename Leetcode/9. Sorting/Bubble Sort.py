def bubble_sort(nums):
    tamanho = len(nums)

    for _ in range(tamanho-1):
        for i in range(tamanho-1):
            if nums[i] > nums[i+1]:
                nums[i],nums[i+1] = nums[i+1],nums[i]

    return nums


print(bubble_sort([3,2,1]))