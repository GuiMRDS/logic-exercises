lista = [1, 2, 3, 4, 5]
lista_invert = []

# Saída:
[5, 4, 3, 2, 1]


def Inverter(lista):
    for i in range(len(lista) - 1, -1, -1):
        lista_invert.append(lista[i])

    print(lista_invert)


Inverter(lista)