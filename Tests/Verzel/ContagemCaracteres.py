palavra = "Guilherme"

def ContagemCaracteres(palavra):
    q = len(palavra)
    num = 0

    for i in range(q):
        num = 1 + num
        print(f"{palavra[i]}: ", num)


ContagemCaracteres(palavra)