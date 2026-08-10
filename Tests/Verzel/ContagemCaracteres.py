palavra = "programacao"

def ContagemCaracteres(palavra):
    quantidade = len(palavra)

    for caracter in palavra:
        for n in range(quantidade):
            if n == caracter:
                print(caracter, n)

    return False



print(ContagemCaracteres(palavra))