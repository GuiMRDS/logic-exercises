print("------------ Números Pares em Intervalo ------------")

numero = int(input("Digite o numero: "))
pares = []

for numero in range(1, numero + 1):
    if numero % 2 == 0:
        pares.append(numero)

print(pares)