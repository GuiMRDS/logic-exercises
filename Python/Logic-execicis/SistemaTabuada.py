print("Bem vindo ao sistema Tabuada")

numero = input("Digite o numero da tabuada: ")

while numero.lower() != "s":
    numero = int(numero)
    for i in range(0, 11):
        print(numero, " X ", i, " = ", numero * i)

    print("\n")
    numero = input("Digite o numero da tabuada ou digite s para sair: ")