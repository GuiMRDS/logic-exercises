

def divisao(n1, n2):
    try:
        print(n1/n2)
    except ZeroDivisionError as erro:
        print("Divisão Invalida")
        print(erro)

divisao(10,0)