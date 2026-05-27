print(" ------------------ Agenda ------------------ ")
print()

AGENDA = {}
AGENDA['guilherme'] = {
    "telefone": "99999-9999",
    "email": "guimars22@gmail.com",
    "endereco": "Rua 28",
}
AGENDA['giulia'] = {
    "telefone": "99999-8888",
    "email": "giulia@gmail.com",
    "endereco": "Rua 33",
}

def mostrarContatos():
    for contato in AGENDA:
        print("Nome:     ", contato)
        print("Telefone: ", AGENDA[contato]["telefone"])
        print("Email:    ", AGENDA[contato]["email"])
        print("Endereço: ", AGENDA[contato]["endereco"])
        print('-------------------------------------')
        print()


mostrarContatos()