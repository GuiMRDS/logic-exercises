const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

console.log("_________ Digite seu login _________");

const senhaCorreta = 123456;

function perguntarSenha() {
  rl.question("Digite sua senha: ", function (senha) {
    senha = Number(senha);

    if (senha === senhaCorreta) {
      console.log("Acesso permitido");

      rl.close();
    } else {
      console.log("Acesso negado");

      perguntarSenha();
    }
  });
}

perguntarSenha();
