numero1 = int(input("Digite um numero: "))
numero2 = int(input("Digite um numero: "))
numero3 = int(input("Digite um numero: "))

if numero1 > numero2 and numero1 > numero3:
    print("Maior numero: " + str(numero1))
elif numero2 > numero1 and numero2 > numero3:
    print("Maior numero: " + str(numero2))
else:
    print("Maior numero: " + str(numero3))

