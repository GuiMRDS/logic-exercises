print(" ------------------ Agenda ------------------ ")

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
    print('-------------------------------------')


def incluirEditarContatos(contato, telefone, email, endereco):
    AGENDA[contato] = {
        "telefone": telefone,
        "email": email,
        "endereco": endereco,
    }
    print(f">>>>>>>>>>>> Contato {contato} adicioando|editado com sucesso =)")
    print('-------------------------------------')


def excluirContato(contato):
    AGENDA.pop(contato)
    print(f">>>>>>>>>>>> Contato {contato} excluido com sucesso =(")
    print('-------------------------------------')


def  imprimir_menu():
    print('-------------------------------------')
    print(' 1 - Mostrar contatos na Agenda ')
    print(' 2 - Buscar contatos na Agenda ')
    print(' 3 - Incluir contatos na Agenda ')
    print(' 4 - Editar contatos na Agenda ')
    print(' 5 - Excluir contatos na Agenda ')
    print(' 0 - Sair da Agenda ')
    print('-------------------------------------')


while True:
    imprimir_menu()
    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        print()
        mostrarContatos()

    elif opcao == '2':
        contato = input("Digite o nome do contato: ")
        print()
        buscarContatos(contato)

    elif opcao == '3':
        print()
        contato = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        email = input("Digite o email do contato: ")
        endereco = input("Digite o endereço do contato: ")
        incluirEditarContatos(contato, telefone, email, endereco)

    elif opcao == '4':
        print()
        contato = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        email = input("Digite o email do contato: ")
        endereco = input("Digite o endereço do contato: ")
        incluirEditarContatos(contato, telefone, email, endereco)

    elif opcao == '5':
        print()
        contato = input("Digite o nome do contato: ")
        excluirContato(contato)

    elif opcao == '0':
        print('Saindo do programa')
        break

    else:
        print("Opção invalida!")