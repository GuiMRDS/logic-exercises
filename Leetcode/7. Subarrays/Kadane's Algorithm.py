array = [-2,1,-3,4,-1,2,1,-5,4]

# Resposta:
# 6

def kadaneSum(arr):
    res = arr[0]

    for i in range(1, len(arr)):
        currSum = 0

        for j in range(i, len(arr)):
            currSum = currSum + arr[j]

            res = max(res, currSum)

    return res


print(kadaneSum(array))