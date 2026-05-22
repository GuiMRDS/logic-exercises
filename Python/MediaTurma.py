print(" --------- Medias dos alunos --------- ")

quantidadeAlunos = int(input("Quantidade de alunos na turma: "))
AlunosAprovados = []
AlunosReprovados = []
notas = []
medias = 0

for i in range(quantidadeAlunos):
    notas.append(float(input("Digite sua nota: ")))

media = sum(notas)/float(quantidadeAlunos)

for nota in notas:
    if nota >= 7:
        AlunosAprovados.append(nota)
    elif nota <= 7:
        AlunosReprovados.append(nota)

print("Media da turma: ", float(media))
print("Alunos Aprovados: ", AlunosAprovados)
print("Alunos Reprovados: ", AlunosReprovados)