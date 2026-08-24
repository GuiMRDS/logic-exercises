array = [2, 3, 1, 2, 4, 3]
target = 7

# Saída:
# 2

def SlidingWindow(array, target):
    esquerda = 0
    soma = 0
    menor = float("inf")

    for direita in range(len(array)):
        soma += array[direita]

        while soma >= target:
            menor = min(menor, direita - esquerda + 1)

            soma -= array[esquerda]
            esquerda += 1

    return menor if menor != float("inf") else 0


def SlidingWindow2(array, k):
    left = 0
    suma = 0
    menor = float("inf")

    for right in range(len(array)):
        suma += array[right]

        while suma >= target:
            menor = min(menor, right - left + 1)
            left -= array[left]
            left += 1

    return menor if menor != float("inf") else 0



print(SlidingWindow(array, target))
print(SlidingWindow2(array, target))