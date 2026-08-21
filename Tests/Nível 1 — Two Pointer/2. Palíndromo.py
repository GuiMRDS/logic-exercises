# Entrada: "racecar"
# Saída: true

# Entrada: "hello"
# Saída: false


def TwoPointer(palavra):
    left = 0
    right = len(palavra)-1

    while left < right:
        if palavra[left] == palavra[right]:
            return True

        left += 1
        right -= 1

    return False



palavra = input("Digite uma palavra: ")
print(TwoPointer(palavra))