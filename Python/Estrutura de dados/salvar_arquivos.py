try:
    with open('nomes.txt') as arquivos:
        print(arquivos.readline())
except Exception as error:
    print('Algum erro foi encontrado!')
    print(error)
