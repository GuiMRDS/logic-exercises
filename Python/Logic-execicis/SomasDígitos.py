print(" --------- Numero Positivo --------- ")

numero = int(input("Entrada: "))
soma = []

for i in range(numero):
    numero = int(input("Digite um numero: "))
    soma.append(numero)

resultado = sum(soma)

print(soma)
print(resultado)