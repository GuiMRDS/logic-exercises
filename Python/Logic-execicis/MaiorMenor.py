print(" ---------------- Digite 10 numeros ---------------- ")

numeros = []
numeroMaior = 0
numeroMenor = 0

for numero in range(10):
    numeros.append(int(input("Digite um numero: ")))

    numeroMaior = numeros[0]
    numeroMenor = numeros[0]

for numero in numeros:
    if numero > numeroMaior:
        numeroMaior = numero
    if numero < numeroMenor:
        numeroMenor = numero

print("Maior numero é: ", numeroMaior)
print("Menor numeor é: ", numeroMenor)