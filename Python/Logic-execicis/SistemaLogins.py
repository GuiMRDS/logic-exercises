print("-------------- LOGIN --------------")

usuario = input("Digite seu usuario: ")
senha = input("Digite sua senha: ")

login = "Gui"
loginSenha = "12345"

while usuario != login or senha != loginSenha:
    print("Usuario ou Senha incorreta")
    usuario = input("Digite seu usuario: ")
    senha = input("Digite sua senha: ")

print("Acesso permitido")