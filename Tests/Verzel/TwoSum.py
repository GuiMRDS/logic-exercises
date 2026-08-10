###
# Input:
nums = [2, 7, 11, 15]
target = 9

# Output:
# [0, 1]
###

def twoSum(nums, target):
    n = len(nums)

    for i in range(n):
        for j in range(n):
            if nums[i] + nums[j] == target:
                return [i, j]

    return False

if __name__ == '__main__':
    distances = twoSum(nums, target)
    print(distances)