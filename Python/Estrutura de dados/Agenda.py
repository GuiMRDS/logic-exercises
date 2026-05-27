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
        buscarContatos(contato)
        print('-------------------------------------')
        print()


def buscarContatos(contato):
    print("Nome:     ", contato)
    print("Telefone: ", AGENDA[contato]["telefone"])
    print("Email:    ", AGENDA[contato]["email"])
    print("Endereço: ", AGENDA[contato]["endereco"])


def incluirEditarContatos(contato, telefone, email, endereco):
    AGENDA[contato] = {
        "telefone": telefone,
        "email": email,
        "endereco": endereco,
    }
    print(f">>>>>>>>>>>> Contato {contato} adicioando|editado com sucesso =)")
    print()




mostrarContatos()
incluirEditarContatos("marcella", "92313-2990", 'marcella@gmail.com', 'Rua 3')
incluirEditarContatos("guilherme", "95555-5550", 'guimars22@gmail.com', 'Rua 7')
mostrarContatos()
excluirContato('marcella')
mostrarContatos()

## buscarContatos('guilherme')

