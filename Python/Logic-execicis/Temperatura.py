print(" --------------- Temperatura --------------- ")

diasTemperatura = []
maiorTemperatura = 0
menorTemperatura = 0
mediaTemperatura = 0
quantidadeDiasAcimaMedia = []

for i in range(10):
    temperatura = float(input("Digite o valor da temperatura: "))
    diasTemperatura.append(temperatura)

for dia in diasTemperatura:
    if dia < maiorTemperatura:
        maiorTemperatura = dia
    elif dia > menorTemperatura:
        menorTemperatura = dia

mediasTemperatura = sum(diasTemperatura) / 10

for dia in diasTemperatura:
    if mediasTemperatura < dia:
        quantidadeDiasAcimaMedia.append(dia)

print("Maior temperatura: ", maiorTemperatura)
print("Menor temperatura: ", menorTemperatura)
print("Media de temperatura: ", mediasTemperatura)
print("Quantidade de dias: ", quantidadeDiasAcimaMedia)