# "radar" → True
# "python" → False

palavra = "radar"

def Palindromo(palavra):
    palavra_invertida = ""

    for letra in palavra:
        palavra_invertida = letra + palavra_invertida
        if palavra == palavra_invertida:
            return True

    return False


print(Palindromo(palavra))