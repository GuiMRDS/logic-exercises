numeros = []
soma = 0

for i in range(5):
    numeros.append(int(input("Digite um numero: ")))

for numero in numeros:
    soma += numero

print(soma)