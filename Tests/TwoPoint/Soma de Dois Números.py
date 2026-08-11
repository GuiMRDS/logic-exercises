nums = [1, 2, 4, 7, 11, 15]
target = 15

# Saída:
(2, 4)

def SomaDoisNumeros(nums):
    n = len(nums)

    for i in range(n):
        for j in range(n):
            if nums[i] + nums[j] == target:
                print(f"{nums[i]} + {nums[j]} = {nums[i] + nums[j]}")


SomaDoisNumeros(nums)