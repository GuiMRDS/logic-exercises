# Entrada: "racecar"
# Saída: true

# Entrada: "hello"
# Saída: false

palavra = "racecar"

def Palindromo(palavras):
    left = 0
    right = len(palavras)-1

    while left < right:
        if palavras[left] == palavras[right]:
            return True

        left += 1
        right -= 1

    return False


print(Palindromo(palavra))