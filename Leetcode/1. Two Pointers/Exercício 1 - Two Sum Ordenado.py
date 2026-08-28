nums = [1,2,4,6,10]
target = 8

# Resposta:
# [2,3]


def TwoPointer(nums):
    left, right = 0, len(nums)-1

    while left <= right:
        soma=nums[left] + nums[right]

        if soma == target:
            return [left, right]

        elif soma < target:
            left += 1

        else:
            right -= 1

    return None


print(TwoPointer(nums))