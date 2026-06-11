print("Soma infinita de numeros")

numero = int(input("Digite um numero: "))
numeros = []
numerosPositivos = []
numerosNegativos = []

while True:
    numero = int(input("Digite numeros e digite 0 quando quiser encerrar: "))
    numeros.append(numero)

    if numero == 0 :
        break

    numeros.append(numero)

for numero in numeros:
    if numero > 0 :
        numerosPositivos.append(numero)
    elif numero < 0 :
        numerosNegativos.append(numero)

print("\n")
print("Total de numero: ", numeros)
print("Total de numero positivos: ", numerosPositivos)
print("Total de numero negativos: ", numerosNegativos)