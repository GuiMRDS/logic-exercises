login = input("Login: ")
senha = input("Senha: ")

senhaCorreta = "12345"

while senha != senhaCorreta:
    senha = input("Senha: ")

    if senha == senhaCorreta:
        print("Acesso permitido")
        break
    else:
        print("Senha incorreta")