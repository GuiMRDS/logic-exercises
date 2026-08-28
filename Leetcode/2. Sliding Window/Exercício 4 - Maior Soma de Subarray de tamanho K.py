nums = [2,1,5,1,3,2]
k = 3

# Resposta:
# 9


def SlidingWindow(nums):
    esquerda, direita = 0, 0
    _max = 1
    counter = {}

    counter[nums[0]] = 1

    while direita < len(nums) - 1:
        direita += 1
        if counter.get(nums[direita]):
            counter[nums[direita]] += 1
        else:
            counter[nums[direita]] = 1

        while counter[nums[direita]] == 3:
            counter[nums[direita]] -= 1
            esquerda += 1

        _max = max(_max, direita-esquerda+1)

    return _max



print(SlidingWindow(nums, k))