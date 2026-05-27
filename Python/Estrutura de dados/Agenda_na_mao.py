AGENDA = {
    "guilherme": {
        "tel": "99119-5225",
        "email": "guimars22@gmail.com",
        "endereço": "Alamenda do Cravo e Rosa"

    },
    "giulia": {
        "tel": "99999-8888",
        "email": "giulia@gmail.com",
        "endereço": "Alamenda das Rosas"

    },
    "isabela": {
        "tel": "96767-5555",
        "email": "isabela04@gmail.com",
        "endereço": "Alamenda dos Cravos"

    },
}

AGENDA['guilherme']['endereço'] = "Rua das nações"

AGENDA['marcella'] = {
    "telefone": "98885-2313",
    "email": "marcella@gmail.com",
    "endereço": "Av votoratin"
}

AGENDA.pop("marcella")

for contato in AGENDA:
    print(contato)
