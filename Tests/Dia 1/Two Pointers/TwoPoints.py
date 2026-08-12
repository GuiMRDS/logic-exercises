a = [1,2,3,4,5]
b = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
c = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
d = [1,2,3,4,5,6,7,8,9,10,]
nums = [1, 2, 4, 7, 11, 15]

palavra = "radar"


def somar(nums, target):
    n = len(nums)

    for i in range(n):
        for j in range(n):
            if nums[i] + nums[j] == target:
                return [i, j]


def palavraReversa(palavra):
    palavra_inversa = ""

    for letra in palavra:
        palavra_inversa = letra + palavra_inversa
        if palavra == palavra_inversa:
            print(palavra_inversa)
            return True

    print(palavra_inversa)
    return False


palavraReversa(palavra)





