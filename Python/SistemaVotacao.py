print(" ------------------ Sistema Votacao ------------------ ")

voto = 0
votoCanditado1 = 0
votoCanditado2 = 0
votoCanditado3 = 0
votoBranco = 0
votoNulo = 0

numeroEleitores = int(input("Digite o numero de eleitores: "))

for i in range(numeroEleitores):
    print("Canditado 1, vote: 1 \n"
          "Canditado 2, vote: 2 \n"
          "Canditado 3, vote: 3 \n"
          "Voto em Branco, vote: 0 \n"
          "Voto nulo, vote: ... \n")

    voto = int(input("Voto: "))

    match voto:
        case 1:
            votoCanditado1 += 1
        case 2:
            votoCanditado2 +=  1
        case 3:
            votoCanditado3 += 1
        case 0:
            votoBranco += 1
        case _:
            votoNulo += 1

if votoCanditado1 > votoCanditado2 and votoCanditado1 > votoCanditado3:
    vercedor = "Cantidado 1"
elif votoCanditado2 > votoCanditado1 and votoCanditado2 > votoCanditado3:
    vercedor = "Cantidado 2"
elif votoCanditado3 > votoCanditado1 and votoCanditado3 > votoCanditado2:
    vercedor = "Cantidado 3"
else:
    vercedor = "Empate"


print("Canditado vencedor:  ", vercedor)
print("Total Votos: ", votoCanditado1)
print("Total Votos: ", votoCanditado2)
print("Total Votos: ", votoCanditado3)
print("Total nulo: ", votoNulo)
print("Voto em Branco: ", votoBranco)
