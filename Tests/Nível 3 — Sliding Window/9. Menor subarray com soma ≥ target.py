array = [2, 3, 1, 2, 4, 3]
target = 7

# Saída:
# 2

def SlidingWindow(array, target):
    left = 0
    soma = 0
    menor = float("inf")

    for direita in range(len(array)):
        soma += array[direita]

        while soma >= target:
            menor = min(menor, direita - left + 1)

            soma -= array[left]
            left += 1

    return menor if menor != float("inf") else 0


print(SlidingWindow(array, target))