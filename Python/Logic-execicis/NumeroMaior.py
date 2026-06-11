numeros = []

for i in range(3):
    numeros.append(int(input("Digite um numero: ")))

maior = numeros[0]

for numero in numeros:
    if numero > maior:
        maior = numero

print("Maior numero: ", maior)