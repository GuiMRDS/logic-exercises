entrada = "python"

# Saída:
True

def Palindromo(entrada):
    palavra_invertida = ""

    for letra in entrada:
        palavra_invertida = letra + palavra_invertida
        if  letra == palavra_invertida:
            return False

    return True


print(Palindromo(entrada))