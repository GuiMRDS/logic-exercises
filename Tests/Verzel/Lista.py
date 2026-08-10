numbers = [10, 5, 8, 20, 3, 20, 15]

def AnalisarLista(numbers):
    maiorNumero = 0
    menorNumero = 0
    soma = 0
    mediaLista = 0
    segundoMaiorNumero = 0

    for i in range(len(numbers)):
        if numbers[i] > maiorNumero:
            maiorNumero = numbers[i]
            menorNumero = i
        if numbers[i] < maiorNumero:
            segundoMaiorNumero = numbers[i]


    mediaLista = sum(numbers) / len(numbers)

    print("maior numero: ", maiorNumero)
    print("menor numero: ", menorNumero)
    print("média: ", mediaLista)
    print("segundo maior número:" , segundoMaiorNumero)


AnalisarLista(numbers)