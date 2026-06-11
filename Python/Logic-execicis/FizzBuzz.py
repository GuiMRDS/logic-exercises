print(" ---------- FIZZ BUZZ --------- ")

entrada = int(input("Digite a entrada: "))
lista = []

for i in range(entrada):
    lista.append(int(input("Digite um valor: ")))

print(lista)

for valor in lista:
    if valor % 3 == 0:
        lista.append("Fizz")
    elif valor % 5 == 0:
        lista.append("Buzz")

print(lista)