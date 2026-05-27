print("Caixa Eletronico")
valor = 2000
print("Valor atual:", valor)

while True:
    saque = input(
        "Digite o valor do saque ou 's' para sair: "
    )

    if saque == "s":
        print("Valor atual:", valor)
        print("SAIR")
        break

    saque = int(saque)

    if saque > valor:
        print("Saldo insuficiente")

    else:
        valor -= saque
        print("Valor do saque:", saque)
        print("Saldo atual:", valor)

    print("\n")