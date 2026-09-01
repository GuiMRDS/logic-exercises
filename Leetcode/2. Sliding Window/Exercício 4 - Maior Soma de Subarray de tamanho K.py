nums = [2,1,5,1,3,2]
k = 3

# Resposta:
# 9


def sliding_window(nums, k):
    esquerda = 0
    direita = k - 1

    soma_atual = sum(nums[:k])
    maior_soma = soma_atual

    while direita < len(nums) - 1:
        direita += 1

        # Adiciona o novo elemento que entrou na janela
        soma_atual += nums[direita]

        # Remove o elemento que saiu da janela
        soma_atual -= nums[esquerda]

        esquerda += 1

        maior_soma = max(maior_soma, soma_atual)

    return maior_soma


print(sliding_window(nums, k))