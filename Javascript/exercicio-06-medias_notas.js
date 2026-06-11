const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

console.log("_________ MEDIAS ALUNOS _________");

function perguntarInformacoes() {
  rl.question("Nome do aluno: ", function (nome) {
    rl.question("Digite a nota do primeiro semestre: ", function (nota1) {
      rl.question("Digite a nota do segundo semestre: ", function (nota2) {
        nota1 = Number(nota1);
        nota2 = Number(nota2);

        let media = (nota1 + nota2) / 2;

        if (media >= 7) {
          console.log("O aluno " + nome + " está APROVADO com média: " + media);
        } else if (media >= 5 && media < 7) {
          console.log(
            "O aluno " + nome + " está de RECUPERAÇÃO com média: " + media,
          );
        } else {
          console.log(
            "O aluno " + nome + " está REPROVADO com média: " + media,
          );
        }

        rl.close();
      });
    });
  });
}

perguntarInformacoes();
