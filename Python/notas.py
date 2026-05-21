print("----------------------- Media da notas -----------------------")

notas = []
media = 0
soma = 0

for i in range(1, 5):
    notas.append(input("Digite a notas: "))
for nota in notas:
    soma += float(nota)

media = soma / 4

if media >= 7:
    print("Aprovado")
elif media >= 5 and media < 6.9:
    print("Recuperação")
elif media < 5.8:
    print("Reprovado")
else:
    print("Error")