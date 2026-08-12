nums = [1,2,4,8,16,32,64,128]
target = 64

# saida
# 6

def exponential_search(nums, target):
    if nums[0] == target:
        return 0
    low = len(nums)
    high = 1

    while high <= low: