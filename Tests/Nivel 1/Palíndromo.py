# Entrada: "racecar"
# Saída: true

# Entrada: "hello"
# Saída: false

entrada = input()

def palindromo(entrada):
    esquerda = 0
    direita = len(entrada) - 1

    while esquerda < direita:
        if entrada[esquerda] != entrada[direita]:
            return False

        esquerda += 1
        direita -= 1

    return True


print(palindromo(entrada))