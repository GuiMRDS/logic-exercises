numbers = [10, 5, 8, 20, 3, 20, 15]


def AnliseLista(numbers):
    maiorNum(numbers)
    menorNum(numbers)
    mediaNum(numbers)


def maiorNum(nums):
    num1 = 0
    num2 = 0

    for num in nums:
        if num > nums[0]:
            num2 = num
            print("Maior numero: ", num2)
            if num > nums[0]:
                num1 = num
                print("Segundo Maior numero: ", num1)
                break



def menorNum(nums):

    for num in nums:
        if num < nums[0]:
            print("Menor numero: ", num)
            break


def mediaNum(nums):
    soma = 0

    for num in nums:
        soma += num

    print("Media: ", soma / len(nums))


AnliseLista(numbers)