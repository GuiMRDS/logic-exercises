print(" ------------------ Agenda ------------------ ")

AGENDA = {}

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


def lerDetalhesContatos():
    telefone = input("Digite o telefone do contato: ")
    email = input("Digite o email do contato: ")
    endereco = input("Digite o endereco do contato: ")
    return telefone, email, endereco


def incluirEditarContatos(contato, telefone, email, endereco):
    AGENDA[contato] = {
        "telefone": telefone,
        "email": email,
        "endereco": endereco,
    }
    salvarAgenda()
    print()
    print(f">>>>>>>>>>>> Contato {contato} adicioando|editado com sucesso =)")
    print('-------------------------------------')


def excluirContato(contato):
    try:
        AGENDA.pop(contato)
        salvarAgenda()
        print(f">>>>>>>>>>>> Contato {contato} excluido com sucesso =(")
        print('-------------------------------------')
    except KeyError:
        print('>>>>>>>>>>>> Contato inexistente')
    except Exception as error:
        print('>>>>>>>>>>>> Um erro ocorreu')
        print(error)


def  imprimir_menu():
    print(' 1 - Mostrar importar na Agenda ')
    print(' 2 - Buscar importar na Agenda ')
    print(' 3 - Incluir importar na Agenda ')
    print(' 4 - Editar importar na Agenda ')
    print(' 5 - Excluir importar na Agenda ')
    print(' 6 - Exportar importar na Agenda para CSV')
    print(' 7 - Importat importar na Agenda para CSV')
    print(' 0 - Sair da Agenda ')
    print('-------------------------------------')


def exportar_contatos(filename):
    try:
        with open('agenda.txt', 'w') as file:
            for contato in AGENDA:
                telefone = AGENDA[contato]["telefone"]
                email = AGENDA[contato]['email']
                endereco = AGENDA[contato]['endereco']
                file.write("{};{};{};{}\n".format(contato, telefone, email, endereco))
        print('>>>>>>>>>>>> Agenda exporado com sucesso =) ')
    except Exception as error:
        print('>>>>>>>>>>>> Erro ao exportar importar')
        print(error)


def importar_contatos(filename):
    try:
        with open('agenda.txt', 'r') as filename:
            linhas = filename.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(';')
                print(detalhes)
                nome = detalhes[0]
                telefone = detalhes[0]
                email = detalhes[0]
                endereco = detalhes[0]

                incluirEditarContatos(nome, telefone, email, endereco)

    except FileNotFoundError:
        print('>>>>>>>>>>>>>>> Erro ao ler ou encontrar o arquivo')

    except Exception as error:
        print('>>>>>>>>>>>>>>> Erro inesperador ocorreu')
        print(error)


def salvarAgenda():
    exportar_contatos('database.csv')


def carregarAgenda():
    importar_contatos('databae.csv')


## Inicio do programa
carregarAgenda()
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
            telefone, email, endereco = lerDetalhesContatos()
            incluirEditarContatos(telefone, email, endereco)

    elif opcao == '4':
        print()
        contato = input("Digite o nome do contato: ")

        try:
            print('>>>>>>>>>>>> Edidando contato: ', contato)
            telefone, email, endereco = lerDetalhesContatos()
            incluirEditarContatos(telefone, email, endereco)

        except KeyError:
            print('>>>>>>>>>>>> Contato inexistente!')

    elif opcao == '5':
        print()
        contato = input("Digite o nome do contato: ")
        excluirContato(contato)

    elif opcao == '6':
        print()
        exportar_contatos(filename)

    elif opcao == '7':
        print()
        filename = input("Digite o nome do arquivo a ser importado: ")
        importar_contatos(filename)

    elif opcao == '0':
        print('Saindo do programa')
        break

    else:
        print("Opção invalida!")