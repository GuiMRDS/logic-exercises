print("Digite 10 valores: ")
numeros = []
numeroPares = []
numeroImpar = []

for i in range(20):
    numeros.append(int(input("Digite um numero: ")))

for numero in numeros:
    if numero % 2 == 0:
        numeroPares.append(numero)
    else:
        numeroImpar.append(numero)

print("Numeros pares: ", numeroPares)
print("Numeros impar: ", numeroImpar)
