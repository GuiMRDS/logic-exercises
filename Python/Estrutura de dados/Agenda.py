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
    if len(AGENDA) > 0:
        for contato in AGENDA:
            buscarContatos(contato)
            print('-------------------------------------')
            print()
    else:
        print('>>>>>>>>>>>> Agenda vazia!')


def buscarContatos(contato):
    try:
        print("Nome:     ", contato)
        print("Telefone: ", AGENDA[contato]["telefone"])
        print("Email:    ", AGENDA[contato]["email"])
        print("Endereço: ", AGENDA[contato]["endereco"])
        print('-------------------------------------')
    except KeyError:
        print('>>>>>>>>>>>> Contato inexistente')
    except Exception as error:
        print('>>>>>>>>>>>> Um erro ocorreu')
        print(error)


def incluirEditarContatos(contato):
    telefone = input("Digite o telefone do contato: ")
    email = input("Digite o email do contato: ")
    endereco = input("Digite o endereco do contato: ")


    AGENDA[contato] = {
        "telefone": telefone,
        "email": email,
        "endereco": endereco,
    }
    print(f">>>>>>>>>>>> Contato {contato} adicioando|editado com sucesso =)")
    print('-------------------------------------')

def excluirContato(contato):
    try:
        AGENDA.pop(contato)
        print(f">>>>>>>>>>>> Contato {contato} excluido com sucesso =(")
        print('-------------------------------------')
    except KeyError:
        print('>>>>>>>>>>>> Contato inexistente')
    except Exception as error:
        print('>>>>>>>>>>>> Um erro ocorreu')
        print(error)


def  imprimir_menu():
    print('-------------------------------------')
    print(' 1 - Mostrar contatos na Agenda ')
    print(' 2 - Buscar contatos na Agenda ')
    print(' 3 - Incluir contatos na Agenda ')
    print(' 4 - Editar contatos na Agenda ')
    print(' 5 - Excluir contatos na Agenda ')
    print(' 6 - Exportar contatos na Agenda ')
    print(' 0 - Sair da Agenda ')
    print('-------------------------------------')


def exportar_contatos():
    try:
        with open('agenda.txt', 'w') as file:
            for contato in AGENDA:
                telefone = AGENDA[contato]["telefone"]
                email = AGENDA[contato]['email']
                endereco = AGENDA[contato]['endereco']
                file.write("{};{};{};{}\n".format(contato, telefone, email, endereco))
        print('>>>>>>>>>>>> Agenda exporado com sucesso =) ')
    except Exception as error:
        print('>>>>>>>>>>>> Erro ao exportar contatos')
        print(error)



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

        try:
            print('>>>>>>>>>>>> Contato já existente!')
        except KeyError:
            incluirEditarContatos(contato)

    elif opcao == '4':
        print()
        contato = input("Digite o nome do contato: ")
        incluirEditarContatos(contato)

        try:
            print('>>>>>>>>>>>> Edidando contato: ', contato)

        except KeyError:
            print('>>>>>>>>>>>> Contato inexistente!')

    elif opcao == '5':
        print()
        contato = input("Digite o nome do contato: ")
        excluirContato(contato)

    elif opcao == '6':
        print()
        exportar_contatos()

    elif opcao == '0':
        print('Saindo do programa')
        break

    else:
        print("Opção invalida!")