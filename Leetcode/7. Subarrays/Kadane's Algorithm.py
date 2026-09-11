array = [-2,1,-3,4,-1,2,1,-5,4]

# Resposta:
# 6

def algorithmKadaneSum(array):
    res = array[0]

    for i in range(1, len(array)):
        currSum = 0

        for j in range(i, len(array)):
            currSum = currSum + array[j]

            res = max(res, currSum)

    return res


def algorithmKadaneSum2(array):
    res = array[0]

    for i in range(1, len(array)):
        currSum = 0

        for j in range(i, len(array)):
            currSum = currSum + array[j]

            res = max(res, currSum)

    return res


print(algorithmKadaneSum(array))
print(algorithmKadaneSum2(array))