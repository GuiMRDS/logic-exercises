numeros = []
positivos = []

for i in range(1, 11):
    numeros.append(int(input("Digite um numero: ")))

for numero in numeros:
    if numero >= 0:
        positivos.append(numero)

print(positivos)