height = [1,8,6,2,5,4,8,3,7]

def CountWaters(height):
    n = len(height)

    for i in range(n):
        for j in range(n):
            if height[j] > height[i]:
                maiorNumero = height[j]
                segundoMaiorNumero = height[i]


    area = maiorNumero * maiorNumero
    print("maior área possível: ",area)


CountWaters(height)